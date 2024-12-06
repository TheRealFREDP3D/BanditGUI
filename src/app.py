"""
Imports the Flask web framework, as well as the `render_template`,
`session`, and `request` modules from Flask. These imports are used
throughout the Flask application to handle web requests, manage
session data, and render HTML templates.
"""

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

import os
from .ssh_manager import SSHManager
from .bandit_levels import BANDIT_LEVELS
from .password_manager import PasswordManager
from .chat_manager import ChatManager

# Creates a new Flask application instance with the name of the current
# module (`__name__`). This is the main entry point for the Flask web
# application and is used to handle incoming HTTP requests, render templates,
# and manage the application's configuration.

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)
socketio = SocketIO(app)

# Create manager instances
ssh_manager = SSHManager()
password_manager = PasswordManager()
chat_manager = ChatManager()


@app.route("/")
def index():
    return render_template("index.html", levels=BANDIT_LEVELS)


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
    """Send the user's progress information."""
    emit("progress_update", password_manager.get_progress())


@socketio.on("get_password")
def handle_get_password(data):
    """Get the saved password for a specific level."""
    level = data.get("level")
    if level is not None:
        emit("password_info", password_manager.get_password(level))


@socketio.on("disconnect")
def handle_disconnect():
    """Clean up SSH connection on disconnect."""
    ssh_manager.disconnect(request.sid)


@socketio.on("chat_message")
def handle_chat_message(data):
    """Handle incoming chat messages."""
    try:
        message = data.get("message", "").strip()
        if not message:
            return

        # Get response from chat manager
        response = chat_manager.get_response(message)

        # Send response back to client
        emit(
            "chat_response",
            {
                "message": response,
                "type": "assistant",
            },
        )

    except Exception as e:
        emit(
            "chat_response",
            {
                "message": f"Error processing message: {str(e)}",
                "type": "error",
            },
        )


if __name__ == "__main__":
    try:
        socketio.run(app, debug=True, port=8080)
    except Exception as e:
        print(f"Error starting server: {str(e)}")
