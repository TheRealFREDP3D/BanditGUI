import os
from dotenv import load_dotenv

load_dotenv()


class CommandHelp:
    def __init__(self):
        self.command_help = {
            "ls": "List directory contents",
            "cd": "Change directory",
            "cat": "Display file contents",
            "file": "Determine file type",
            "du": "Estimate file space usage",
            "find": "Search for files",
            "grep": "Search text patterns",
            "sort": "Sort text lines",
            "uniq": "Report or filter out repeated lines",
            "strings": "Print printable strings",
            "base64": "Base64 encode/decode",
            "tr": "Translate characters",
            "tar": "Tape archiving utility",
            "gzip": "Compress files",
            "bzip2": "Block-sorting file compressor",
            "xxd": "Hexdump or reverse hexdump",
            "mkdir": "Make directories",
            "cp": "Copy files and directories",
            "mv": "Move files and directories",
            "ssh": "OpenSSH remote login client",
            "nc": "Netcat for reading/writing network connections",
            "nmap": "Network exploration and security scanning",
            "diff": "Compare files line by line",
            "cron": "Daemon to execute scheduled commands",
        }
        self.command_examples = {
            "ls": """```# List files in current directory
ls

# List all files (including hidden)
ls -la

# List files with human-readable sizes
ls -lh
```""",
            "cd": """```# Go to home directory
cd ~

# Go up one directory
cd ..

# Go to specific directory
cd /path/to/directory
```""",
            "cat": """```# Display file contents
cat filename

# Display file with line numbers
cat -n filename

# Display multiple files
cat file1 file2
```""",
            "ssh": """```# Connect to remote server
ssh username@hostname

# Connect on specific port
ssh -p 2220 username@hostname

# Use specific key file
ssh -i keyfile username@hostname
```""",
        }

    def get_command_help(self, command):
        if command not in self.command_help:
            return f"Sorry, I don't have specific help for the `{command}` command."

        base_help = self.command_help[command]
        examples = self.command_examples.get(
            command, "```\n# Basic usage\n" + command + "\n```"
        )

        response = f"""# `{command}` Command Help

## Description
{base_help}

## Common Usage
{examples}

## Tips
- Use `man {command}` for the full manual
- Use `{command} --help` for quick help
"""
        return response


class APIManager:
    def __init__(self):
        self.api_key = os.getenv("GITHUB_TOKEN")
        if not self.api_key:
            raise ValueError("GITHUB_TOKEN environment variable is not set.")
        self.base_url = "https://models.inference.ai.azure.com"
        self.model = "Meta-Llama-3.1-70B-Instruct"

    def get_headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }


class ChatManager:
    def __init__(self, command_help, api_manager):
        self.command_help = command_help
        self.api_manager = api_manager
        self.system_prompt = """You are an expert CTF (Capture The Flag) assistant, specifically knowledgeable about the OverTheWire Bandit challenges. 
        Your role is to help users learn and solve challenges without giving direct answers. 
        Provide hints, explain Unix commands, and guide users through problem-solving steps.
        Focus on teaching security concepts and Linux command line skills.
        
        Format your responses using markdown:
        - Use # for main headings
        - Use ## for subheadings
        - Use ``` for code blocks
        - Use * or - for bullet points
        - Use `code` for inline code
        - Use numbered lists for steps
        """

    def generate_response(self, user_message, current_level=0):
        message_lower = user_message.lower()
        try:
            from bandit_levels import BANDIT_LEVELS
        except ImportError:
            return "Error: Could not import BANDIT_LEVELS from bandit_levels module."

        level_info = BANDIT_LEVELS.get(current_level, {})

        if "objective" in message_lower or "goal" in message_lower:
            return self._generate_level_objective(level_info)

        elif "hint" in message_lower or "help" in message_lower:
            return self._generate_level_hints(level_info)

        elif any(cmd in message_lower for cmd in self.command_help.command_help.keys()):
            return self._generate_command_help(message_lower)

        elif "how" in message_lower:
            return self._generate_level_guidance(level_info)

        return self._generate_default_response()

    def _generate_level_objective(self, level_info):
        return f"""# Level {level_info.get('level', 'Unknown')} Objective

{level_info.get('objective', 'Complete the level challenges.')}

## Description
{level_info.get('description', 'No additional description available.')}"""

    def _generate_level_hints(self, level_info):
        hints = level_info.get("hints", [])
        if hints:
            return f"""# Level {level_info.get('level', 'Unknown')} Hints

{chr(10).join(['- ' + hint for hint in hints])}

Need more specific help? Try:
- Ask about the level objective
- Use `!help <command>` for command help
- Ask about specific concepts"""
        return "No hints available for this level."

    def _generate_command_help(self, message_lower):
        for cmd in self.command_help.command_help.keys():
            if cmd in message_lower:
                return self.command_help.get_command_help(cmd)
        return "Command not found."

    def _generate_level_guidance(self, level_info):
        return f"""# Level {level_info.get('level', 'Unknown')} Guidance

## Objective
{level_info.get('objective', 'Complete the level challenges.')}

## Useful Commands
{chr(10).join(['- `' + cmd + '`: ' + self.command_help.command_help.get(cmd, '') for cmd in level_info.get('useful_commands', [])])}

Need more help? Try:
- Ask for hints
- Use `!help <command>` for detailed command help
- Ask about specific concepts"""

    def _generate_default_response(self):
        return f"""# Bandit Level Assistant

I can help you with:

1. Level Information
   - Type "objective" to see the level goal
   - Type "hint" for helpful hints
   - Ask "how" for solving guidance

2. Command Help
   - Use `!help <command>` for detailed help
   - Example: `!help ls` for help with ls command

3. Specific Questions
   - Ask about any Linux command
   - Ask about concepts you don't understand
   - Ask for clarification on level details

What would you like to know about?
"""


# Dependency Injection
command_help = CommandHelp()
api_manager = APIManager()
chat_manager = ChatManager(command_help, api_manager)

# Example usage
user_message = "Can you give me a hint for level 1?"
response = chat_manager.generate_response(user_message, current_level=1)
print(response)
