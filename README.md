**BanditGUI: A Web-Based GUI for OverTheWire Bandit**

**Overview**

BanditGUI is a web application that provides a graphical user interface for the OverTheWire Bandit wargame. It simplifies the learning process by offering an integrated terminal, level-specific instructions and hints, a helpful chat assistant, and progress tracking.

**Features**

* **Integrated Web Terminal:** Interact with the Bandit levels directly within your browser.
* **Level Instructions and Hints:** Get clear guidance for each level, including objectives, descriptions, and hints.
* **AI-Powered Chat Assistant:** Ask questions, get command explanations, and receive contextual help without revealing the answers.
* **Progress Tracking:** Monitor your progress through the Bandit levels.
* **Password Management:** Securely store and retrieve discovered passwords.

**Installation**

1. **Clone the repository:**

   ```bash
   git clone https://github.com/TheRealFredP3D/BanditGUI.git
   cd BanditGUI
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   Create a `.env` file in the project root and add your API key for the chat assistant (if using an external API):

   ```
   GITHUB_API_KEY=your_api_key_here
   ```

4. **Run the application:**

   ```bash
   python app.py
   ```

5. **Open in your browser:**
   Navigate to `http://127.0.0.1:5000/`

**Usage**

1. Select a Bandit level from the level selection menu.
2. Use the integrated terminal to execute commands and solve the challenges.
3. Interact with the chat assistant for hints and guidance.
4. Track your progress as you complete the levels.

**Strengths**

* **Integrated SSH Management:** Efficient SSH connection management with `paramiko`.
* **Password Management:** Secure storage and tracking of discovered passwords.
* **Level Information and Hints:** Structured information about each level, including descriptions, objectives, and hints.
* **Interactive Chat Assistant:** Basic chat assistant with keyword matching and pre-defined responses.
* **Real-time Terminal Output:** Flask-SocketIO enables real-time output from SSH sessions in the web terminal.

**Weaknesses**

* **Hardcoded API Key:** Previously used a hardcoded API key; now uses environment variables (but ensure `.env` is not committed to version control).
* **Limited Chat Functionality:** Basic chat assistant; consider integrating a more powerful NLP model.
* **Incomplete Level Data:** Only provides information for the first few Bandit levels; needs to be completed for all 34 levels.
* **Error Handling:** Basic error handling; consider implementing more specific error messages and handling different exception types.
* **Security Concerns (OpenSSL usage):** Relies on `openssl s_client` for levels 16 and 17; ensure server certificate verification to prevent man-in-the-middle attacks.

**Roadmap**

* **Complete Level Data:** Add complete information for all 34 Bandit levels.
* **Enhanced Chat Assistant:** Integrate a more powerful NLP model for more intelligent and contextual responses.
* **Improved Error Handling:** Provide more specific error messages and handle different exception types.
* **Dynamic Level Loading:** Load level data dynamically from the JSON file.
* **User Authentication:** Implement user authentication to store individual progress and preferences.
* **Frontend Enhancements:** Improve the web interface with better styling and more interactive elements.
* **Integrated Command Execution History:** Store and display the user's command history within the web terminal.
* **Challenge Completion Verification:** Implement a way to verify if the user has actually completed a level.

**Contributing**

Contributions are welcome! Please feel free to open issues and submit pull requests.

**License**

This project is licensed under the MIT License. See the [Apache-2.0](LICENSE) file for details.
