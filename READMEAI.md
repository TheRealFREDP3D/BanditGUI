<p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center">BANDITGUI.GIT</h1></p>
<p align="center">
	<em>Conquer Bandit, level up your skills.
</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/therealfredp3d/banditgui.git?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/therealfredp3d/banditgui.git?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/therealfredp3d/banditgui.git?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/therealfredp3d/banditgui.git?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

## 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
  - [🧪 Testing](#🧪-testing)
- [📌 Project Roadmap](#-project-roadmap)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

BanditGUI simplifies OverTheWire Bandit walkthroughs with a web interface.  It provides an interactive terminal for SSH commands, automated password management, progress tracking, and an AI-powered chat assistant offering hints and explanations.  Ideal for cybersecurity learners, it enhances the learning experience by combining practical exercises with guided support.

---

## 👾 Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Client-server architecture: A web frontend (`templates/index.html`) interacts with a Python backend (`app.py`).</li><li>Modular design:  Functionality is separated into modules like `SSHManager`, `PasswordManager`, and `ChatManager` for maintainability.</li><li>Uses `Flask` <tool> as the web framework and `Flask-SocketIO` <tool> for real-time communication.</li><li>Data persistence: User progress is stored in `user_progress.json` and level data in `bandit_levels.json` and `BANDIT_LEVELS.json`.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Code style and adherence to best practices are unknown without further inspection.</li><li>The use of separate modules suggests an attempt at good organization.</li><li>Error handling is mentioned in `fetch_bandit_levels.py`, indicating some consideration for robustness.</li><li>Further analysis is needed to assess code quality metrics like cyclomatic complexity and code coverage.</li></ul> |
| 📄 | **Documentation** | <ul><li>Primary language is Python, with supplementary JSON and HTML files.</li><li>Limited documentation within the code itself; relies heavily on file names and comments for understanding.</li><li>Installation instructions are provided using `pip` <tool> and `requirements.txt`.</li><li>The documentation could be significantly improved with more comprehensive docstrings and external documentation.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrates with `Paramiko` <tool> for SSH interaction.</li><li>Uses a CTF assistant API (details unspecified) within `chat_manager.py`.</li><li>Uses `Python-dotenv` <tool> for environment variable management.</li><li>Scrapes data from the OverTheWire Bandit website (`fetch_bandit_levels.py`).</li></ul> |
| 🧩 | **Modularity**    | <ul><li>The codebase is divided into several modules (e.g., `ssh_manager.py`, `password_manager.py`, `chat_manager.py`).</li><li>This modularity promotes reusability and maintainability.</li><li>Dependencies are managed via `requirements.txt`.</li><li>Further analysis is needed to assess the level of coupling between modules.</li></ul> |
| 🧪 | **Testing**       | <ul><li>Testing is suggested by the presence of `pytest` <tool> in the test commands.</li><li>The extent of test coverage is unknown without further investigation.</li><li>No specific test files are mentioned in the provided context.</li><li>Comprehensive testing is crucial for ensuring the reliability and stability of the application.</li></ul> |

---

## 📁 Project Structure

```sh
└── banditgui.git/
    ├── .github
    │   └── ISSUE_TEMPLATE
    ├── CODE_OF_CONDUCT.md
    ├── CONTRIBUTING.md
    ├── LICENSE
    ├── README.md
    ├── ROADMAP.md
    ├── SECURITY.md
    ├── app.py
    ├── assets
    │   ├── ui.png
    │   └── virtual-assistant.jpg
    ├── bandit_levels.py
    ├── chat_header.md
    ├── chat_manager.py
    ├── docs
    │   ├── Files-BANDIT_LEVELS.py.md
    │   ├── Files-chat_manager.py.md
    │   ├── Files-ssh_manager.py.md
    │   ├── Files-templates_index.html.md
    │   ├── Flowchart-Login-Form.md
    │   ├── Flowchart-Monitor_Output_For_Password.md
    │   ├── Flowchart-SocketIO-Events.md
    │   ├── Flowchart-ssh_manager.py.md
    │   ├── Project-Overview-2.md
    │   ├── Project-Overview.md
    │   ├── assets
    │   ├── v1.0-Review-Cline.md
    │   └── v1.0-Review-Gemini.md
    ├── levels
    │   ├── BANDIT_LEVELS.json
    │   └── bandit-website-data
    ├── password_manager.py
    ├── requirements.txt
    ├── ssh_manager.py
    ├── static
    │   ├── .gitkeep
    │   ├── css
    │   └── text
    ├── templates
    │   └── index.html
    └── user_progress.json
```


### 📂 Project Index
<details open>
	<summary><b><code>BANDITGUI.GIT/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/therealfredp3d/banditgui.git/blob/master/ssh_manager.py'>ssh_manager.py</a></b></td>
				<td>- SSHManager provides a centralized interface for managing multiple SSH connections<br>- It handles connection establishment, command execution, and disconnection, ensuring thread safety<br>- The module stores connection credentials and allows for both individual and bulk connection closures, simplifying SSH interaction within the larger application.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/therealfredp3d/banditgui.git/blob/master/bandit_levels.py'>bandit_levels.py</a></b></td>
				<td>- The `bandit_levels.py` file defines a data structure containing information about different levels in a cybersecurity training game (likely OverTheWire Bandit)<br>- It acts as a central repository for level descriptions, objectives, hints, and resources, enabling the game to dynamically present challenges to the user<br>- The file's purpose within the overall project is to manage and organize the game's levels, making them easily accessible and modifiable.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/therealfredp3d/banditgui.git/blob/master/password_manager.py'>password_manager.py</a></b></td>
				<td>- PasswordManager facilitates persistent storage and retrieval of passwords within a game<br>- It securely saves discovered passwords to a JSON file, enabling progress tracking across game levels<br>- The module verifies user-provided outputs against expected passwords, updating the saved progress accordingly and providing functions to check level completion and retrieve passwords.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/therealfredp3d/banditgui.git/blob/master/user_progress.json'>user_progress.json</a></b></td>
				<td>- User progress tracking is managed via a JSON file<br>- It stores user-specific data, in this case, a single entry linking a user identifier ("bandit0") to a corresponding value ("bandit0")<br>- This suggests a system for recording and potentially retrieving user-related information within a larger application<br>- The file's role is fundamental to maintaining individual user progress within the application's overall architecture.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/therealfredp3d/banditgui.git/blob/master/chat_manager.py'>chat_manager.py</a></b></td>
				<td>- ChatManager facilitates interaction with a CTF assistant<br>- It leverages an API for responses and a CommandHelp module for Unix command explanations<br>- The system guides users through OverTheWire Bandit challenges by providing hints, objectives, and command usage instructions, focusing on educational aspects rather than direct solutions<br>- Environment variables manage API key access.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/therealfredp3d/banditgui.git/blob/master/app.py'>app.py</a></b></td>
				<td>- The application provides a web interface for SSH server interaction and chat<br>- It facilitates remote command execution, password management across multiple levels, progress tracking, and AI-powered chat support via a real-time interface<br>- User credentials are used to establish SSH connections, and the system automatically detects and saves passwords discovered during command execution<br>- Progress is tracked and displayed, enhancing user experience.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/therealfredp3d/banditgui.git/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td>- `requirements.txt` specifies the project's dependencies<br>- It ensures Flask (a web framework), Paramiko (for SSH), Python-dotenv (for environment variables), and Flask-SocketIO (for real-time communication) are installed at the correct versions<br>- This file is crucial for reproducible builds and consistent environment setup across different machines, supporting the overall web application architecture.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- levels Submodule -->
		<summary><b>levels</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/therealfredp3d/banditgui.git/blob/master/levels/BANDIT_LEVELS.json'>BANDIT_LEVELS.json</a></b></td>
				<td>- BANDIT_LEVELS.json defines the structure for a cybersecurity training game<br>- It outlines individual levels, providing descriptions, objectives, hints, and helpful commands for each stage<br>- The data facilitates a progressive learning experience, guiding users through increasingly complex challenges to achieve the overall game objective<br>- Each level's information enhances the game's educational value.</td>
			</tr>
			</table>
			<details>
				<summary><b>bandit-website-data</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/therealfredp3d/banditgui.git/blob/master/levels/bandit-website-data/fetch_bandit_levels.py'>fetch_bandit_levels.py</a></b></td>
						<td>- The script retrieves data for OverTheWire Bandit challenge levels<br>- It scrapes level descriptions, objectives, and hints from the OverTheWire website, structuring this information into a JSON file<br>- This JSON file, `bandit_levels.json`, is then used to provide a structured representation of the challenge levels for other parts of the project<br>- Error handling ensures robustness against website changes or network issues.</td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<details> <!-- templates Submodule -->
		<summary><b>templates</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/therealfredp3d/banditgui.git/blob/master/templates/index.html'>index.html</a></b></td>
				<td>- The `templates/index.html` file serves as the main user interface for the Bandit CTF Learning Assistant<br>- It's a frontend HTML template that uses external libraries to create a user experience incorporating a terminal emulator and markdown rendering, likely for displaying challenge information and user interaction<br>- The inclusion of Socket.IO suggests real-time communication with a backend server for challenge updates and feedback<br>- In essence, this file defines the visual layout and interactive elements of the application's user interface.</td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with banditgui.git, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip


### ⚙️ Installation

Install banditgui.git using one of the following methods:

**Build from source:**

1. Clone the banditgui.git repository:
```sh
❯ git clone https://github.com/therealfredp3d/banditgui.git
```

2. Navigate to the project directory:
```sh
❯ cd banditgui.git
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```




### 🤖 Usage
Run banditgui.git using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


### 🧪 Testing
Run the test suite using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```


---
## 📌 Project Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/therealfredp3d/banditgui.git/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/therealfredp3d/banditgui.git/issues)**: Submit bugs found or log feature requests for the `banditgui.git` project.
- **💡 [Submit Pull Requests](https://github.com/therealfredp3d/banditgui.git/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/therealfredp3d/banditgui.git
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/therealfredp3d/banditgui.git/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=therealfredp3d/banditgui.git">
   </a>
</p>
</details>

---

## 🎗 License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 🙌 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---
