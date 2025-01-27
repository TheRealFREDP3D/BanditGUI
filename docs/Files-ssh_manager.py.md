# BanditGUI - ssh_manager.py

The `SSHManager` class is designed to manage SSH connections and execute commands over those connections. Here's a breakdown of its components and functionality:

<!-- file: f:\BACKUP\FRED\PROJECTS\_GITHUB-TheRealFredP3D\BanditGUI\_PUBLIC-v1.1-Final\ssh_manager.py -->
```python
class SSHManager:
    def __init__(self):
        self.connections: Dict[str, paramiko.SSHClient] = {}
        self.credentials: Dict[str, Dict[str, str]] = {}
        self.lock = threading.Lock()
```

- **Constructor (`__init__`)**: Initializes the class with:
  - `connections`: A dictionary to store active SSH connections, keyed by `session_id`.
  - `credentials`: A dictionary to store SSH credentials associated with each session.
  - `lock`: A threading lock to ensure thread-safe operations on shared resources.

```python
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
```

- **Connect Method (`connect`)**: Securely connects to an SSH server, storing the connection and credentials.
  - Uses Paramiko for the SSH connection.
  - Reuses the `lock` to ensure thread safety.
  - Closes any existing connections before establishing a new one for the given `session_id`.
  - Sets a policy to automatically add the SSH server's host key.

```python
self.credentials[session_id] = {
    'username': username,
    'password': password,
    'host': host,
    'port': port
}
return True
```

- **Credentials Storage**: Stores the provided credentials for the session after a successful connection attempt.

```python  
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
        result = error if error else output
        if not result.endswith('\n'):
            result += '\n'
        return result.replace('\n', '\r\n')
```

- **Command Execution (`execute_command`)**: Executes a command on an SSH server.
  - Retrieves the connection using the `session_id`, and throws an exception if there is no active connection.
  - Executes the command and captures the output and any errors.
  - Adjusts line endings for proper display in a terminal.

```python
def disconnect(self, session_id: str):
    """Close a specific SSH connection"""
    with self.lock:
        if session_id in self.connections:
            try:
                self.connections[session_id].close()
                del self.connections[session_id]
                self.credentials.pop(session_id, None)
            except Exception as e:
                print(f"Error disconnecting: {str(e)}")
```

- **Disconnect Method (`disconnect`)**: Closes an active SSH connection.
  - Ensures thread safety using the lock.
  - Handles exceptions during disconnection and removes the session's data from the dictionaries.

The class is critical for managing SSH connections in a secure and isolated manner, ensuring that commands are executed in a controlled environment per session.
