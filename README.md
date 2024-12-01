# Bandit CTF Learning Platform

An interactive web-based platform designed to help users learn Linux security through the OverTheWire Bandit CTF challenges.

## Features

- **Interactive Terminal**: Secure SSH connection to Bandit servers
- **Smart Chat Assistant**: Context-aware help system with markdown support
- **Command Reference**: Color-coded command list with detailed explanations
- **Progress Tracking**: Automatic password saving and level progression
- **Dark Theme UI**: Modern, responsive interface optimized for learning

## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/BanditGUI.git
cd BanditGUI
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to `http://localhost:5000`

## Usage

1. **Connect to a Level**
   - Enter your Bandit username and password
   - Click the connect button to establish SSH connection

2. **Terminal Commands**
   - Use the terminal interface to enter Linux commands
   - Click the keyboard icon or press `Ctrl+K` to view command reference

3. **Get Help**
   - Use the chat interface to ask questions
   - Type `!help <command>` for specific command help
   - Ask about level objectives and hints

## Key Components

- **Flask Backend**: Handles web server and WebSocket connections
- **SSH Manager**: Manages secure connections to Bandit servers
- **Chat Manager**: Provides contextual help and guidance
- **Password Manager**: Tracks level progress and passwords

## Security Features

- Secure SSH connection handling
- No storage of sensitive credentials
- Safe password management for level progression

## UI/UX Features

- Responsive dark theme design
- Command categorization
- Helpful tooltips and popups
- Markdown-formatted responses
- Intuitive chat interface

## Available Commands

Access the command reference by:
- Clicking the keyboard icon
- Using the `!help` command in chat
- Pressing `Ctrl+K`

## Contributing

Contributions are welcome! Please feel free to submit pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OverTheWire for the Bandit wargame
- Flask and Flask-SocketIO teams
- Paramiko SSH library developers
