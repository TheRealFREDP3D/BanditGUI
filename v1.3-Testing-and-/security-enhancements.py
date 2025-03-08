# Enhanced SSH Service with improved security
import paramiko
import threading
import time
from typing import Dict, Optional, Tuple
import logging
from cryptography.fernet import Fernet
import os

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PasswordManager:
    """Handles secure storage and retrieval of sensitive credentials"""
    
    def __init__(self):
        # Generate or load encryption key
        key_path = os.path.join(os.path.dirname(__file__), '../data/.key')
        if os.path.exists(key_path):
            with open(key_path, 'rb') as f:
                self.key = f.read()
        else:
            self.key = Fernet.generate_key()
            os.makedirs(os.path.dirname(key_path), exist_ok=True)
            with open(key_path, 'wb') as f:
                f.write(self.key)
        
        self.cipher = Fernet(self.key)
    
    def encrypt(self, password: str) -> bytes:
        """Encrypt a password"""
        return self.cipher.encrypt(password.encode())
    
    def decrypt(self, encrypted_password: bytes) -> str:
        """Decrypt an encrypted password"""
        return self.cipher.decrypt(encrypted_password).decode()

class SSHConnection:
    def __init__(self, hostname: str, port: int, username: str, password: str):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.client = None
        self.channel = None
        self.connected = False
        self.lock = threading.Lock()
        self.last_activity = time.time()
        self.timeout = 300  # 5 minutes inactive timeout
        
    def connect(self) -> bool:
        """Establish SSH connection to the Bandit server with enhanced security checks"""
        try:
            self.client = paramiko.SSHClient()
            
            # Added security: Use system host keys
            self.client.load_system_host_keys()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            # Connection timeout
            self.client.connect(
                hostname=self.hostname,
                port=self.port,
                username=self.username,
                password=self.password,
                look_for_keys=False,
                allow_agent=False,
                timeout=10
            )
            
            self.channel = self.client.invoke_shell()
            self.channel.settimeout(30)
            self.connected = True
            self.last_activity = time.time()
            
            # Clear initial banner
            time.sleep(1)
            self.channel.recv(4096).decode('utf-8')
            
            # Start idle timeout monitor
            threading.Thread(target=self._monitor_idle_timeout, daemon=True).start()
            
            logger.info(f"Successfully connected to {self.hostname} as {self.username}")
            return True
        except paramiko.AuthenticationException:
            logger.error(f"Authentication failed for {self.username}@{self.hostname}")
            return False
        except paramiko.SSHException as e:
            logger.error(f"SSH error: {str(e)}")
            return False
        except Exception as e:
            logger.error(f"Connection error: {str(e)}")
            return False
    
    def _monitor_idle_timeout(self):
        """Monitor connection for idle timeout"""
        while self.connected:
            time.sleep(60)  # Check every minute
            if time.time() - self.last_activity > self.timeout:
                logger.info(f"Connection {self.username}@{self.hostname} timed out due to inactivity")
                self.disconnect()
                break
    
    def disconnect(self) -> None:
        """Close SSH connection"""
        if self.channel:
            self.channel.close()
        if self.client:
            self.client.close()
        self.connected = False
        logger.info(f"Disconnected from {self.hostname} as {self.username}")
    
    def execute_command(self, command: str) -> str:
        """Execute a command with input sanitization and return the output"""
        with self.lock:
            if not self.connected or not self.channel:
                raise Exception("Not connected to SSH server")
            
            # Updated: Sanitize command input
            sanitized_command = self._sanitize_command(command)
            if sanitized_command != command:
                logger.warning(f"Command was sanitized: {command} -> {sanitized_command}")
                command = sanitized_command
            
            # Update last activity time
            self.last_activity = time.time()
            
            # Send command
            self.channel.send(command + "\n")
            
            # Wait for output
            time.sleep(0.5)
            output = ""
            while self.channel.recv_ready():
                chunk = self.channel.recv(4096).decode('utf-8')
                output += chunk
                if not self.channel.recv_ready():
                    time.sleep(0.1)  # Small delay to ensure all data is received
            
            return output
    
    def _sanitize_command(self, command: str) -> str:
        """Basic command sanitization to prevent command injection"""
        # Block certain dangerous commands
        dangerous_commands = [
            'rm -rf', 'sudo', ':(){:|:&};:', '> /dev/sda', 
            'mkfs', 'dd if=/dev/zero', 'shutdown', 'reboot'
        ]
        
        for dangerous in dangerous_commands:
            if dangerous in command:
                return "echo 'Command blocked for security reasons'"
        
        return command

class SSHManager:
    def __init__(self):
        self.connections: Dict[str, SSHConnection] = {}
        self.password_manager = PasswordManager()
    
    def create_connection(self, session_id: str, level: int, password: str) -> bool:
        """Create a new SSH connection for a specific session and level"""
        hostname = "bandit.labs.overthewire.org"
        port = 2220
        username = f"bandit{level}"
        
        # Store the password securely
        encrypted_password = self.password_manager.encrypt(password)
        
        conn = SSHConnection(hostname, port, username, password)
        success = conn.connect()
        
        if success:
            self.connections[session_id] = conn
            # Security: Log connection success without password
            logger.info(f"Created connection for session {session_id} to level {level}")
        else:
            # Security: Log failed connection without password
            logger.warning(f"Failed to create connection for session {session_id} to level {level}")
        
        return success
    
    def close_connection(self, session_id: str) -> None:
        """Close an existing SSH connection"""
        if session_id in self.connections:
            self.connections[session_id].disconnect()
            del self.connections[session_id]
            logger.info(f"Closed connection for session {session_id}")
    
    def execute_command(self, session_id: str, command: str) -> Tuple[str, bool]:
        """Execute a command on a specific session and check for level completion"""
        if session_id not in self.connections:
            return "Not connected to the server. Please reconnect.", False
        
        try:
            output = self.connections[session_id].execute_command(command)
            
            # Check if this command revealed a password (level completion)
            level_completed = self.check_for_password(output)
            
            return output, level_completed
        except Exception as e:
            logger.error(f"Error executing command in session {session_id}: {str(e)}")
            return f"Error executing command: {str(e)}", False
    
    def check_for_password(self, output: str) -> bool:
        """Check if output contains a potential password for the next level"""
        import re
        # Looking for strings that look like passwords (alphanumeric, 10-32 chars)
        password_pattern = r'\b[a-zA-Z0-9]{10,32}\b'
        potential_passwords = re.findall(password_pattern, output)
        
        return len(potential_passwords) > 0
    
    def cleanup_idle_connections(self) -> None:
        """Clean up idle connections that haven't been properly closed"""
        for session_id, connection in list(self.connections.items()):
            if time.time() - connection.last_activity > connection.timeout:
                logger.info(f"Cleaning up idle connection for session {session_id}")
                self.close_connection(session_id)

# Singleton instance
ssh_manager = SSHManager()

# Schedule periodic cleanup
def start_cleanup_scheduler():
    def cleanup_task():
        while True:
            time.sleep(300)  # Run every 5 minutes
            ssh_manager.cleanup_idle_connections()
    
    cleanup_thread = threading.Thread(target=cleanup_task, daemon=True)
    cleanup_thread.start()

# Start the cleanup scheduler
start_cleanup_scheduler()
