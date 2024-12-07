#!/usr/bin/env python3

# ------------------------------------------------ *
# Author: Frederick Pellerin                     --- *
# Email:  fredp3d@proton.me                         --- *
# Repo:   https://Github.com/TheRealFredP3D/BanditGUI --- *
# --------------------------------------------------------- *
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
    Starts the Flask-SocketIO server on port 5000 with debug mode.
    """
    try:
        socketio.run(app, debug=True, port=5000, host="0.0.0.0")
    except Exception as e:
        print(f"Error starting BanditGUI: {str(e)}")
        return 1
    return 0


if __name__ == "__main__":
    exit(main())
