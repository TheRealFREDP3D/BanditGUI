import pytest
from flask import Flask
from flask_socketio import SocketIO, emit
from app import app, socketio, ssh_manager, password_manager

@pytest.fixture
def client():
    test_client = app.test_client()
    return test_client

@pytest.fixture
def socketio_client(client):
    return socketio.test_client(app, flask_test_client=client)

def test_connect_ssh(socketio_client):
    # Test successful connection
    socketio_client.emit('connect_ssh', {'username': 'testuser', 'password': 'testpass'})
    received = socketio_client.get_received()
    assert any(event['name'] == 'ssh_connected' for event in received)

    # Test unsuccessful connection
    socketio_client.emit('connect_ssh', {'username': '', 'password': ''})
    received = socketio_client.get_received()
    assert any(event['name'] == 'ssh_error' for event in received)

def test_ssh_command(socketio_client):
    socketio_client.emit('ssh_command', {'command': 'echo "Hello"', 'current_level': 0})
    received = socketio_client.get_received()
    assert any(event['name'] == 'terminal_output' for event in received)

def test_get_progress(socketio_client):
    socketio_client.emit('get_progress')
    received = socketio_client.get_received()
    assert any(event['name'] == 'progress_update' for event in received)

def test_get_saved_password(socketio_client):
    socketio_client.emit('get_saved_password', {'level': 0})
    received = socketio_client.get_received()
    assert any(event['name'] == 'password_info' for event in received)

def test_chat_message(socketio_client):
    socketio_client.emit('chat_message', {'message': 'Hello'})
    received = socketio_client.get_received()
    assert any(event['name'] == 'chat_response' for event in received)