"""
This Flask application provides a web-based interface for interacting with an SSH server and managing chat conversations.

The main features of the application include:
- Establishing SSH connections to the server using provided credentials
- Executing commands on the remote server and displaying the output
- Detecting and saving passwords for subsequent levels
- Tracking the user's progress through the levels
- Providing a chat interface for interacting with an AI-powered chat manager

The application uses the Flask web framework, the Flask-SocketIO library for real-time communication, and various custom modules to handle the SSH connections, password management, and chat functionality.
"""

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import os
from ssh_manager import SSHManager
from bandit_levels import BANDIT_LEVELS
from password_manager import PasswordManager
from chat_manager import ChatManager, APIManager, ChatManager, CommandHelp
from dotenv import load_dotenv

load_dotenv()

# Initialize Flask and SocketIO

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)
socketio = SocketIO(app)

# Create manager instances
ssh_manager = SSHManager()
password_manager = PasswordManager()
command_help = CommandHelp()
api_manager = APIManager()
chat_manager = ChatManager(command_help, api_manager)

# Route for the main page


@app.route("/")
def index():
    return render_template("index.html", levels=BANDIT_LEVELS)


# SocketIO event handlers
@socketio.on("connect_ssh")
def handle_ssh_connection(data):
    try:
        username = data.get("username")
        password = data.get("password")
        session_id = request.sid

        if not username or not password:
            emit("ssh_error", {"message": "Please provide both username and password"})
            return

        try:
            ssh_manager.connect(session_id, username, password)

            # Get level number from username (e.g., bandit0 -> 0)
            level = int(username.replace("bandit", ""))
            level_info = BANDIT_LEVELS.get(level, {})

            # Emit event to update level information
            emit("update_level_info", level_info)

            emit(
                "ssh_connected",
                {"message": "Connected successfully", "level_info": level_info},
            )
        except Exception as e:
            emit("ssh_error", {"message": str(e)})

    except Exception as e:
        emit("ssh_error", {"message": f"Connection error: {str(e)}"})


@socketio.on("ssh_command")
def handle_ssh_command(data):
    session_id = request.sid
    command = data.get("command", "").strip()
    current_level = data.get("current_level", 0)

    if not command:
        return

    try:
        # Execute command and get output
        output = ssh_manager.execute_command(session_id, command)

        # Check if the output contains a password
        is_password, password = password_manager.check_output_for_password(
            current_level, output
        )

        if is_password:
            congratulation_msg = {
                "type": "success",
                "message": f"🎉 Congratulations! You've completed level {current_level}!\n"
                f"Password for level {current_level + 1} found: {password}\n"
                f"This password has been saved for future use.",
            }
            emit("notification", congratulation_msg)

            # Also send progress update
            emit("progress_update", password_manager.get_progress())

        # Send the command output to the terminal
        emit("terminal_output", {"output": output})

    except Exception as e:
        emit("terminal_output", {"output": f"Error: {str(e)}\r\n"})


@socketio.on("get_progress")
def handle_get_progress():
    """Send user's progress"""
    emit("progress_update", password_manager.get_progress())


@socketio.on("get_saved_password")
def handle_get_password(data):
    """Get saved password for a level"""
    level = data.get("level", 0)
    password = password_manager.get_password(level)
    emit("password_info", {"level": level, "password": password})


@socketio.on("disconnect")
def handle_disconnect():
    session_id = request.sid
    ssh_manager.disconnect(session_id)


@socketio.on("chat_message")
def handle_chat_message(data):
    try:
        message = data.get("message", "").strip()
        current_level = data.get("current_level", 0)

        if not message:
            return

        # Generate response using chat manager
        response = chat_manager.generate_response(message, current_level)

        # Send response back to client
        emit("chat_response", {"message": response})

    except Exception as e:
        print(f"Error handling chat message: {str(e)}")
        emit(
            "chat_response",
            {
                "message": "I encountered an error processing your message. Please try again."
            },
        )


if __name__ == "__main__":
    try:
        socketio.run(app, debug=True)
    finally:
        ssh_manager.close_all()
