from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit
import paramiko
import os
from ssh_manager import SSHManager
from bandit_levels import BANDIT_LEVELS
from password_manager import PasswordManager

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
socketio = SocketIO(app)

# Create SSH manager instance
ssh_manager = SSHManager()
password_manager = PasswordManager()

@app.route('/')
def index():
    return render_template('index.html', levels=BANDIT_LEVELS)

@socketio.on('connect_ssh')
def handle_ssh_connection(data):
    try:
        username = data.get('username')
        password = data.get('password')
        session_id = request.sid
        
        if not username or not password:
            emit('ssh_error', {'message': 'Please provide both username and password'})
            return
            
        try:
            ssh_manager.connect(session_id, username, password)
            emit('ssh_connected', {'message': 'Connected successfully'})
        except Exception as e:
            emit('ssh_error', {'message': str(e)})
            
    except Exception as e:
        emit('ssh_error', {'message': f'Connection error: {str(e)}'})

@socketio.on('ssh_command')
def handle_ssh_command(data):
    session_id = request.sid
    command = data.get('command', '').strip()
    current_level = data.get('current_level', 0)
    
    if not command:
        return
        
    try:
        # Execute command and get output
        output = ssh_manager.execute_command(session_id, command)
        
        # Check if the output contains a password
        is_password, password = password_manager.check_output_for_password(current_level, output)
        
        if is_password:
            congratulation_msg = {
                'type': 'success',
                'message': f'🎉 Congratulations! You\'ve completed level {current_level}!\n'
                          f'Password for level {current_level + 1} found: {password}\n'
                          f'This password has been saved for future use.'
            }
            emit('notification', congratulation_msg)
            
            # Also send progress update
            emit('progress_update', password_manager.get_progress())
        
        # Send the command output to the terminal
        emit('terminal_output', {'output': output})
        
    except Exception as e:
        emit('terminal_output', {'output': f'Error: {str(e)}\r\n'})

@socketio.on('get_progress')
def handle_get_progress():
    """Send user's progress"""
    emit('progress_update', password_manager.get_progress())

@socketio.on('get_saved_password')
def handle_get_password(data):
    """Get saved password for a level"""
    level = data.get('level', 0)
    password = password_manager.get_password(level)
    emit('password_info', {
        'level': level,
        'password': password
    })

@socketio.on('disconnect')
def handle_disconnect():
    session_id = request.sid
    ssh_manager.disconnect(session_id)

@socketio.on('chat_message')
def handle_chat_message(data):
    message = data['message']
    # TODO: Implement AI chat response
    # For now, just echo back the message
    emit('chat_response', {'response': f'Assistant: I received your message: {message}'})

if __name__ == '__main__':
    try:
        socketio.run(app, debug=True)
    finally:
        ssh_manager.close_all()
