# BanditGUI v1.1 - BANDIT_LEVELS.py

docs/v1.1-BANDIT_LEVELS.py.md

---

******
# TODO - Replace with the `/levels/bandit_levels.json` file
******

---
The `bandit_levels.py` file is a Python dictionary named `BANDIT_LEVELS` that defines metadata for each level of a challenge or game, specifically the OverTheWire Bandit wargame. Each level has the following attributes:

---

### **Structure of Each Level**

- **`level`**: A string that describes the transition between levels (e.g., "Level 0 → Level 1").
- **`description`**: A short description of the current level's challenge.
- **`objective`**: The specific task or goal that needs to be accomplished to complete the level.
- **`hints`**: A list of tips and suggestions to help the player solve the challenge.
- **`useful_commands`**: A list of Linux commands that may be useful for solving the level.
- **`resources`**: A list of external links or documentation that can provide additional information or context.

---

### **Examples of Levels**

#### **Level 0**

- **Description**: Introduces the game and requires the user to log into a server using SSH.
- **Objective**: Connect to the `bandit.labs.overthewire.org` server on port 2220 using the provided username and password.
- **Hints**: Explains basic SSH usage and provides the password.
- **Useful Commands**: `ssh`.
- **Resources**: A link to OverTheWire's Bandit documentation.

---

#### **Level 5 → Level 6**

- **Description**: The challenge involves finding a file with specific properties in the `inhere` directory.
- **Objective**: Locate the file that is human-readable, exactly 1033 bytes in size, and not executable.
- **Hints**: Suggests using the `find` command with conditions and checking file properties.
- **Useful Commands**: `ls`, `find`, `file`.
- **Resources**: A link to the level documentation.

---

#### **Level 13 → Level 14**

- **Description**: Involves using a private SSH key to log in as a new user and read a password file.
- **Objective**: Log in with the private key stored in `~/sshkey.private` and retrieve the password.
- **Hints**: Discusses the use of SSH private keys and adjusting file permissions.
- **Useful Commands**: `ssh`, `chmod`, `cat`.
- **Resources**: Documentation on the level.

---

### **Purpose of the File**

1. **Game Framework**: Provides the backend system with a structured way to serve level-specific information to the frontend.
2. **Guidance for Players**: Supplies hints and resources to help players complete levels.
3. **Dynamic Content Delivery**: Allows the game or application to adapt and provide details for different levels programmatically.

---

### **How It Fits into the Application**

1. **Frontend Integration**:
   - Levels can be displayed dynamically on the user interface.
   - Example: The `index()` function in `app.py` uses this data to render the homepage with level descriptions.

2. **Backend Functionality**:
   - The application references this file in WebSocket events (e.g., `handle_ssh_connection`).
   - The level metadata (e.g., objectives, hints) can be sent to the client for real-time interactions.

---

### **Expansion**

- Adding new levels is straightforward; simply append a new dictionary entry with the same structure.
- Supports integration with a web-based or CLI-based challenge platform.

Let me know if you’d like to see a function to retrieve level data dynamically or to perform validation on the `BANDIT_LEVELS` structure!
