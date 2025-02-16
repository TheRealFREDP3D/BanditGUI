import paramiko
import threading
from typing import Optional, Dict

class SSHManager:
    def __init__(self):
        self.connections: Dict[str, paramiko.SSHClient] = {}
        self.credentials: Dict[str, Dict[str, str]] = {}
        self.lock = threading.Lock()

    def connect(self, session_id: str, username: str, password: str, host: str = 'bandit.labs.overthewire.org', port: int = 2220) -> bool:
        """Connect to SSH server and store the connection"""
        try:
            with self.lock:
                # Close existing connection if any
                if session_id in self.connections:
                    try:
                        self.connections[session_id].close()
                    except:
                        pass
                    del self.connections[session_id]
                    self.credentials.pop(session_id, None)

                # Create new connection
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(
                    hostname=host,
                    port=port,
                    username=username,
                    password=password,
                    timeout=10,
                    allow_agent=False,
                    look_for_keys=False
                )
                
                # Test connection with a simple command
                stdin, stdout, stderr = client.exec_command('echo "test"')
                if stdout.channel.recv_exit_status() != 0:
                    raise Exception("Failed to execute test command")

                self.connections[session_id] = client
                self.credentials[session_id] = {
                    'username': username,
                    'password': password,
                    'host': host,
                    'port': port
                }
                return True
        except paramiko.AuthenticationException:
            print("Authentication failed")
            raise Exception("Authentication failed. Please check your username and password.")
        except paramiko.SSHException as e:
            print(f"SSH exception: {str(e)}")
            raise Exception(f"SSH error: {str(e)}")
        except Exception as e:
            print(f"Failed to connect: {str(e)}")
            raise Exception(f"Connection failed: {str(e)}")

    def execute_command(self, session_id: str, command: str) -> str:
        """Execute command on the SSH connection"""
        if session_id not in self.connections:
            raise Exception("Not connected to SSH server")

        try:
            client = self.connections[session_id]
            stdin, stdout, stderr = client.exec_command(command)
            output = stdout.read().decode('utf-8')
            error = stderr.read().decode('utf-8')
            
            # Ensure proper line endings for terminal display
            result = error or output
            if not result.endswith('\n'):
                result += '\n'
            return result.replace('\n', '\r\n')
        except Exception as e:
            raise Exception(f"Failed to execute command: {str(e)}")

    def disconnect(self, session_id: str):
        """Close a specific SSH connection"""
        with self.lock:
            if session_id in self.connections:
                try:
                    self.connections[session_id].close()
                except Exception:
                    pass  # Ignore errors during close
                del self.connections[session_id]
                self.credentials.pop(session_id, None)

    def close_all(self):
        """Close all SSH connections"""
        with self.lock:
            for client in self.connections.values():
                try:
                    client.close()
                except Exception:
                    pass  # Ignore errors during close
            self.connections.clear()
            self.credentials.clear()
