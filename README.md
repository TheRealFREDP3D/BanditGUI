<p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center"><code>❯ BanditGUI</code></h1></p>
<p align="center">
	<em><code>❯ A modern web-based platform for learning Linux security through OverTheWire Bandit CTF challenges</code></em>
</p>
<p align="center">
	<!-- local repository, no metadata badges. --></p>
<p align="center">Built with the tools and technologies:</p>
<p align="center">
	<img src="https://img.shields.io/badge/Flask-000000.svg?style=default&logo=Flask&logoColor=white" alt="Flask">
	<img src="https://img.shields.io/badge/npm-CB3837.svg?style=default&logo=npm&logoColor=white" alt="npm">
	<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=default&logo=HTML5&logoColor=white" alt="HTML5">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=default&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/Poetry-60A5FA.svg?style=default&logo=Poetry&logoColor=white" alt="Poetry">
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

BanditGUI is an innovative web-based learning platform designed to make learning Linux security more accessible and interactive. Built with Flask and modern web technologies, it provides a seamless interface for connecting to and solving OverTheWire's Bandit CTF (Capture The Flag) challenges. The platform combines an interactive terminal, smart assistance, and progress tracking to create an optimal learning environment for both beginners and intermediate users exploring Linux security concepts.

---

## 👾 Features

- **🔒 Secure SSH Integration**: Direct connection to Bandit servers with secure credential handling
- **💻 Interactive Terminal**: Web-based terminal interface for executing Linux commands
- **🤖 Smart Chat Assistant**: Context-aware help system with markdown support for enhanced learning
- **📚 Command Reference System**: Comprehensive, color-coded command list with detailed explanations
- **📊 Progress Tracking**: Automatic password management and level progression tracking
- **🌙 Modern Dark Theme**: Responsive, user-friendly interface optimized for extended learning sessions
- **📝 Markdown Support**: Rich text formatting for challenge descriptions and help content
- **⌨️ Keyboard Shortcuts**: Efficient access to features like command reference (Ctrl+K)
- **🔍 Contextual Help**: Level-specific guidance and command explanations
- **🔄 Real-time Updates**: WebSocket-based communication for immediate feedback

---

## 📁 Project Structure

```sh
└── /
    ├── .github
    │   ├── ISSUE_TEMPLATE
    │   └── dependabot.yml
    ├── CODE_OF_CONDUCT.md
    ├── CONTRIBUTING.md
    ├── LICENSE
    ├── Pipfile
    ├── Pipfile.lock
    ├── README.md
    ├── SECURITY.md
    ├── __pycache__
    │   ├── __init__.cpython-312.pyc
    │   ├── app.cpython-312.pyc
    │   ├── bandit_levels.cpython-312.pyc
    │   ├── banditgui.cpython-312.pyc
    │   ├── chat_manager.cpython-312.pyc
    │   ├── password_manager.cpython-312.pyc
    │   ├── progress_manager.cpython-312.pyc
    │   └── ssh_manager.cpython-312.pyc
    ├── ├── archive
    │   ├── v1-flowchart.md
    │   ├── v1.1-Final.tar
    │   └── v1.3.1-Working.tar
    ├── banditgui.py
    ├── docs
    │   ├── v1.3-Entity-Relationship-Diagram.md
    │   ├── v1.3-Flowchart.md
    │   ├── v1.3-Project-Overview.md
    │   └── v1.3-Structure.md
    ├── image.png
    ├── package-lock.json
    ├── package.json
    ├── poetry.lock
    ├── pyproject.toml
    ├── readme-ai.md
    ├── requirements.txt
    ├── src
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── app.py
    │   ├── chat_manager.py
    │   ├── levels
    │   ├── password_manager.py
    │   ├── ssh_manager.py
    │   ├── static
    │   └── templates
    ├── tests
    │   ├── __init__.py   
	│   ├── pytest_app.py
    │   ├── test_banditgui.py
    │   └── unittest_app.py
    |── ui.png
    ├── user_progress.json
    └── virtual-assistant.jpg
```

### 📂 Project Index
<details open>
	<summary><b><code>/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='/package-lock.json'>package-lock.json</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='/requirements.txt'>requirements.txt</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='/package.json'>package.json</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='/pyproject.toml'>pyproject.toml</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='/user_progress.json'>user_progress.json</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='/Pipfile'>Pipfile</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='/appmap.yml'>appmap.yml</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='/banditgui.py'>banditgui.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- .github Submodule -->
		<summary><b>.github</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='/.github/dependabot.yml'>dependabot.yml</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- src Submodule -->
		<summary><b>src</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='/src/password_manager.py'>password_manager.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='/src/chat_manager.py'>chat_manager.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='/src/ssh_manager.py'>ssh_manager.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='/src/app.py'>app.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
			<details>
				<summary><b>templates</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='/src/templates/solve_response.txt'>solve_response.txt</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='/src/templates/solve_quotes.txt'>solve_quotes.txt</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='/src/templates/welcome.txt'>welcome.txt</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='/src/templates/solve_quotes_nasty.txt'>solve_quotes_nasty.txt</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='/src/templates/index.html'>index.html</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
					<details>
						<summary><b>style</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='/src/templates/style/main.css'>main.css</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<details>
				<summary><b>levels</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='/src/levels/bandit_levels.json'>bandit_levels.json</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
					<details>
						<summary><b>bandit-website-data</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='/src/levels/bandit-website-data/fetch_bandit_levels.py'>fetch_bandit_levels.py</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with , ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Npm, Pipenv, Pip, Poetry


### ⚙️ Installation

Install  using one of the following methods:

**Build from source:**

1. Clone the  repository:
```sh
❯ git clone https://github.com/TheRealFredP3D/BanditGUI
```

2. Navigate to the project directory:
```sh
❯ cd 
```

3. Install the project dependencies:


**Using `npm`** &nbsp; [<img align="center" src="" />]()

```sh
❯ npm install
```


**Setting the environment and dependencies**

**Using `pipenv`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pipenv-3775A9.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pipenv.pypa.io/)

```sh
❯ pipenv install
```

or

**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```

or

**Using `poetry`** &nbsp; [<img align="center" src="https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json" />](https://python-poetry.org/)

```sh
❯ poetry install
```




### 🤖 Usage
Run  using the following command:

**Using `pipenv`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pipenv-3775A9.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pipenv.pypa.io/)

```sh
❯ pipenv shell
❯ pipenv run python banditgui.py
```

or

**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python banditgui.py
```

or 

**Using `poetry`** &nbsp; [<img align="center" src="https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json" />](https://python-poetry.org/)

```sh
❯ poetry run python banditgui.py
```

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/TheRealFredP3D/BanditGUI/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/TheRealFredP3D/BanditGUI/issues)**: Submit bugs found or log feature requests for the `` project.
- **💡 [Submit Pull Requests](https://github.com/TheRealFredP3D/BanditGUI/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your LOCAL account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/TheRealFredP3D/BanditGUI/
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
6. **Push to LOCAL**: Push the changes to your forked repository.
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
   <a href="https://https://github.com/TheRealFredP3D/BanditGUI/graphs/contributors">
      <img src="https://contrib.rocks/image?repo=https://github.com/TheRealFredP3D/BanditGUI/">
   </a>
</p>
</details>

---

## 🎗 License

This project is protected under the [MIT License](https://choosealicense.com/licenses) License. For more details, refer to the [MIT Lisence](https://choosealicense.com/licenses/) file.

---

## 🙌 Acknowledgments

- Overthewire
- Python, Flask
- CodeSignal, Codedex, Exercism, Cisco, Microsoft Learn
- VSCode
---
