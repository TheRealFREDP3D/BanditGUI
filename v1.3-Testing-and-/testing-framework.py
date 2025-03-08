# tests/test_ssh_service.py
import unittest
from unittest.mock import patch, MagicMock
import paramiko
from app.services.ssh_service import SSHConnection, SSHManager

class TestSSHConnection(unittest.TestCase):
    @patch('paramiko.SSHClient')
    def test_connect_success(self, mock_ssh_client):
        # Setup mocks
        mock_client = MagicMock()
        mock_channel = MagicMock()
        mock_ssh_client.return_value = mock_client
        mock_client.invoke_shell.return_value = mock_channel
        
        # Create connection
        connection = SSHConnection('hostname', 22, 'username', 'password')
        
        # Test connection
        result = connection.connect()
        
        # Assertions
        self.assertTrue(result)
        self.assertTrue(connection.connected)
        mock_client.set_missing_host_key_policy.assert_called_once()
        mock_client.connect.assert_called_once_with(
            hostname='hostname',
            port=22,
            username='username',
            password='password',
            look_for_keys=False,
            allow_agent=False,
            timeout=10
        )
    
    @patch('paramiko.SSHClient')
    def test_connect_failure_auth(self, mock_ssh_client):
        # Setup mocks
        mock_client = MagicMock()
        mock_ssh_client.return_value = mock_client
        mock_client.connect.side_effect = paramiko.AuthenticationException("Auth failed")
        
        # Create connection
        connection = SSHConnection('hostname', 22, 'username', 'wrong_password')
        
        # Test connection
        result = connection.connect()
        
        # Assertions
        self.assertFalse(result)
        self.assertFalse(connection.connected)
    
    @patch('paramiko.SSHClient')
    def test_disconnect(self, mock_ssh_client):
        # Setup mocks
        mock_client = MagicMock()
        mock_channel = MagicMock()
        mock_ssh_client.return_value = mock_client
        mock_client.invoke_shell.return_value = mock_channel
        
        # Create and connect
        connection = SSHConnection('hostname', 22, 'username', 'password')
        connection.connect()
        
        # Test disconnect
        connection.disconnect()
        
        # Assertions
        self.assertFalse(connection.connected)
        mock_channel.close.assert_called_once()
        mock_client.close.assert_called_once()
    
    @patch('paramiko.SSHClient')
    def test_execute_command(self, mock_ssh_client):
        # Setup mocks
        mock_client = MagicMock()
        mock_channel = MagicMock()
        mock_ssh_client.return_value = mock_client
        mock_client.invoke_shell.return_value = mock_channel
        
        # Setup channel to return output
        mock_channel.recv_ready.side_effect = [True, True, False]
        mock_channel.recv.return_value = "Command output".encode()
        
        # Create and connect
        connection = SSHConnection('hostname', 22, 'username', 'password')
        connection.connect()
        
        # Test execute command
        output = connection.execute_command("test command")
        
        # Assertions
        self.assertEqual(output, "Command output" * 2)  # Twice because recv_ready returns True twice
        mock_channel.send.assert_called_once_with("test command\n")
    
    @patch('paramiko.SSHClient')
    def test_command_sanitization(self, mock_ssh_client):
        # Setup mocks
        mock_client = MagicMock()
        mock_channel = MagicMock()
        mock_ssh_client.return_value = mock_client
        mock_client.invoke_shell.return_value = mock_channel
        
        # Create and connect
        connection = SSHConnection('hostname', 22, 'username', 'password')
        connection.connect()
        
        # Test dangerous command
        connection.execute_command("rm -rf /")
        
        # Assert sanitized command was sent
        mock_channel.send.assert_called_once_with("echo 'Command blocked for security reasons'\n")

# tests/test_terminal_service.py
import unittest
from unittest.mock import patch, MagicMock
from app.services.terminal_service import TerminalService

class TestTerminalService(unittest.TestCase):
    @patch('app.services.ssh_service.ssh_manager')
    @patch('app.models.command_history.CommandHistory')
    @patch('app.models.progress.Progress')
    def test_execute_command(self, mock_progress, mock_command_history, mock_ssh_manager):
        # Setup mocks
        mock_ssh_manager.execute_command.return_value = ("Command output", False)
        
        # Create service
        service = TerminalService()
        
        # Test execute command
        output, level_completed = service.execute_command("user1", "session1", "ls")
        
        # Assertions
        self.assertEqual(output, "Command output")
        self.assertFalse(level_completed)
        mock_command_history.add_command.assert_called_once_with("user1", "ls")
        mock_ssh_manager.execute_command.assert_called_once_with("session1", "ls")
    
    @patch('app.services.ssh_service.ssh_manager')
    @patch('app.models.command_history.CommandHistory')
    @patch('app.models.progress.Progress')
    def test_execute_command_level_completed(self, mock_progress, mock_command_history, mock_ssh_manager):
        # Setup mocks
        mock_ssh_manager.execute_command.return_value = ("Output with password: abc123xyz789", True)
        mock_progress.get_current_level.return_value = 0
        
        