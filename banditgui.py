#!/usr/bin/env python3

"""
BanditGUI - Main Entry Point

This is the main entry point for the BanditGUI application. It imports and runs
the Flask application from the src package. This separation allows for better
code organization and maintainability.
"""

from src.app import app, socketio

def main():
    """
    Main function to run the BanditGUI application.
    Starts the Flask-SocketIO server on port 8080 with debug mode.
    """
    try:
        socketio.run(app, debug=True, port=8080)
    except Exception as e:
        print(f"Error starting BanditGUI: {str(e)}")
        return 1
    return 0

if __name__ == "__main__":
    exit(main())
