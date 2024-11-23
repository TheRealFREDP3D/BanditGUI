import paramiko
import threading
from typing import Optional, Dict


class SSHError(Exception):
    """Base exception class for SSH-related errors"""
    pass


class SSHManager:
    def __init__(self):
        self.connections: Dict[str, paramiko.SSHClient] = {}
        self.credentials: Dict[str, Dict[str, str]] = {}
        self.lock = threading.Lock()

    # SSH-specific error messages
    ERROR_MESSAGES = {
        "auth_failed": "Authentication failed. Please check your username and password.",
        "connection_failed": "Unable to establish SSH connection. Please try again.",
        "not_connected": "Not connected to SSH server. Please reconnect.",
        "command_failed": "Failed to execute command. Please try again.",
        "test_failed": "Failed to verify SSH connection.",
    }

    def connect(
        self,
        session_id: str,
        username: str,
        password: str,
        host: str = "bandit.labs.overthewire.org",
        port: int = 2220,
    ) -> bool:
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
                    look_for_keys=False,
                )

                # Test connection with a simple command
                stdin, stdout, stderr = client.exec_command('echo "test"')
                if stdout.channel.recv_exit_status() != 0:
                    raise SSHError("test_failed")

                self.connections[session_id] = client
                self.credentials[session_id] = {
                    "username": username,
                    "password": password,
                    "host": host,
                    "port": port,
                }
                return True
        except paramiko.AuthenticationException:
            print("Authentication failed")
            raise SSHError("auth_failed")
        except paramiko.SSHException as e:
            print(f"SSH exception: {str(e)}")
            raise SSHError("connection_failed")
        except Exception as e:
            print(f"Failed to connect: {str(e)}")
            raise SSHError("connection_failed")

    def execute_command(self, session_id: str, command: str) -> str:
        """Execute command on the SSH connection"""
        if session_id not in self.connections:
            raise SSHError("not_connected")

        try:
            client = self.connections[session_id]
            stdin, stdout, stderr = client.exec_command(command)
            output = stdout.read().decode("utf-8")
            error = stderr.read().decode("utf-8")

            # Ensure proper line endings for terminal display
            result = error if error else output
            if not result.endswith("\n"):
                result += "\n"
            return result.replace("\n", "\r\n")
        except Exception as e:
            print(f"Command execution failed: {str(e)}")
            raise SSHError("command_failed")

    def disconnect(self, session_id: str):
        """Close a specific SSH connection"""
        with self.lock:
            if session_id in self.connections:
                try:
                    self.connections[session_id].close()
                except:
                    pass  # Ignore errors during close
                del self.connections[session_id]
                self.credentials.pop(session_id, None)

    def close_all(self):
        """Close all SSH connections"""
        with self.lock:
            for client in self.connections.values():
                try:
                    client.close()
                except:
                    pass  # Ignore errors during close
            self.connections.clear()
            self.credentials.clear()
