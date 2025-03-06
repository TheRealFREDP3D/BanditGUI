# BanditGUI v1.1 - index.html

`docs/v1.1-templates_index.html`

---

### **Key Features of the HTML File**

#### **1. Real-Time Terminal Interaction**

- **Terminal**:
  - Uses the **Xterm.js** library for a web-based terminal interface.
  - Implements custom event listeners to handle user input and WebSocket communications.
- **WebSocket Integration**:
  - Communicates with the backend server (e.g., Flask app) via **Socket.IO**.
  - Handles events like SSH connection, command execution, and server responses.

#### **2. Challenge Info Panel**

- Displays information about the current challenge:
  - **Level Title**
  - **Description**
  - **Objective**
  - **Hints**
  - **Useful Commands**
  - **External Resources**

#### **3. Chat Assistant**

- **Chat Interface**:
  - Allows users to interact with an assistant for help regarding commands or challenges.
  - Messages are processed and displayed in a styled chat window.
- **Markdown Parsing**:
  - Uses the **Marked.js** library to format assistant responses.

#### **4. Command Reference**

- Provides categorized command references for:
  - **File Operations**
  - **Navigation**
  - **Search & Analysis**
  - **Network Tools**
  - **System & Compression**
- Commands are styled and listed in both the chat and a popup panel.

#### **5. Notifications**

- Dynamic notifications for important updates like progress or errors.

---

### **Notable JavaScript Functionality**

1. **Terminal Setup**:
   - Initializes the Xterm.js terminal.
   - Captures user input to emit `ssh_command` events to the server.

2. **WebSocket Event Handling**:
   - `ssh_connected`: Updates the terminal and challenge panel when a connection is established.
   - `terminal_output`: Outputs server responses in the terminal.
   - `chat_response`: Appends assistant responses to the chat interface.
   - `notification`: Displays alerts for events like connection errors or progress updates.

3. **Challenge Loading**:
   - Dynamically updates the challenge panel based on the current level.
   - Requests saved passwords and progress from the server.

4. **Popup & Tooltip Handling**:
   - Implements toggling for the command reference popup.
   - Adds delayed tooltips for UI elements like the keyboard icon.

---

### **Styling**

- The interface is styled for a dark theme:
  - **Background**: Dark gray and black tones.
  - **Text**: White and blue accents for readability.
  - **Chat and Terminal**: Distinct sections with rounded corners and padding for a clean UI.

---

### **Possible Integrations with the Backend**

- This frontend seamlessly integrates with the provided Flask application:
  - Uses WebSocket events to handle SSH connections, command execution, and user progress.
  - Displays real-time updates and dynamic challenge content based on `bandit_levels.py`.

---
