# BanditGUI - An Interactive CTF Learning Platform

## About

This Flask application integrates Flask-SocketIO for real-time communication and provides features for managing SSH connections, command execution, password handling, and a chat system.

---

### **Imports and Setup**

1. **Flask and Flask-SocketIO**: Used to handle HTTP routes and WebSocket events, enabling real-time client-server communication.
2. **Paramiko**: Likely used for SSH operations (via the `SSHManager`).
3. **Custom Modules**:
   - `SSHManager`: Handles SSH connections and command execution.
   - `PasswordManager`: Manages passwords for different levels.
   - `ChatManager`: Generates responses for chat functionality.
   - `BANDIT_LEVELS`: Contains level-specific metadata, possibly from a game or interactive system.

4. **Flask App Configuration**:
   - `SECRET_KEY`: Protects sessions from tampering.
   - `SocketIO`: Enables WebSocket functionality.

---

### **Key Components**

#### **1. HTTP Route**

- **`@app.route('/')`**:
  - Renders the `index.html` template and passes `BANDIT_LEVELS` to the frontend. This is likely a landing page that displays available levels or instructions.

#### **2. WebSocket Events**

- WebSocket events handle real-time operations for SSH, terminal commands, progress updates, and chat responses.

---

#### **SSH Management**

- **Event: `connect_ssh`**
  - Authenticates a user using credentials (username, password).
  - Connects via `SSHManager` and retrieves level information from `BANDIT_LEVELS`.
  - Emits success or error messages to the client.

- **Event: `ssh_command`**
  - Executes a terminal command for the connected session.
  - If the command's output contains a password (detected by `PasswordManager`), it updates progress and notifies the client.
  - Sends command output to the terminal.

- **Event: `disconnect`**
  - Ensures the user's SSH session is closed when they disconnect.

---

#### **Password Management**

- **Event: `get_progress`**
  - Fetches and emits the user's progress from `PasswordManager`.

- **Event: `get_saved_password`**
  - Retrieves a saved password for a specified level and sends it to the client.

---

#### **Chat System**

- **Event: `chat_message`**
  - Processes user messages with the `ChatManager`.
  - Generates and sends a response based on the current level context.
  - Handles errors gracefully with a default error message.

---

### **Helper Classes**

- **`SSHManager`**: Manages SSH connections for multiple clients using session IDs.
- **`PasswordManager`**: Tracks user progress, stores passwords, and detects passwords in command outputs.
- **`ChatManager`**: Responds to user input with contextually relevant information, likely using predefined responses or AI.

---

### **Execution**

- The app is started with `socketio.run(app, debug=True)` in debug mode for development.
- Upon termination, it ensures all SSH sessions are closed with `ssh_manager.close_all()`.

---

### **Features and Flow**

1. **Login**: Users log in with SSH credentials.
2. **Command Execution**: Commands are sent to the server, executed, and results are returned.
3. **Progress Tracking**: Passwords and levels are managed to track user advancement.
4. **Chat Assistance**: Provides interactive help or feedback during user interaction.
