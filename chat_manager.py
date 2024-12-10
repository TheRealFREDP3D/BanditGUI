import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

class ChatManager:
    def __init__(self):
        self.api_key = os.getenv('GITHUB_API_KEY')
        self.base_url = "https://models.inference.ai.azure.com"
        self.model = "Meta-Llama-3.1-70B-Instruct"
        
        # System prompt for CTF guidance
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
            "cron": "Daemon to execute scheduled commands"
        }

    def get_headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
    def get_command_help(self, command):
        """Get detailed help for a specific command"""
        if command not in self.command_help:
            return f"Sorry, I don't have specific help for the `{command}` command."
            
        base_help = self.command_help[command]
        examples = self.get_command_examples(command)
        
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

    def get_command_examples(self, command):
        """Get examples for specific commands"""
        examples = {
            "ls": """```
# List files in current directory
ls

# List all files (including hidden)
ls -la

# List files with human-readable sizes
ls -lh
```""",
            "cd": """```
# Go to home directory
cd ~

# Go up one directory
cd ..

# Go to specific directory
cd /path/to/directory
```""",
            "cat": """```
# Display file contents
cat filename

# Display file with line numbers
cat -n filename

# Display multiple files
cat file1 file2
```""",
            "ssh": """```
# Connect to remote server
ssh username@hostname

# Connect on specific port
ssh -p 2220 username@hostname

# Use specific key file
ssh -i keyfile username@hostname
```"""
        }
        return examples.get(command, "```\n# Basic usage\n" + command + "\n`")

    def generate_response(self, user_message, current_level=0):
        """Generate a response based on user message"""
        # Convert message to lowercase for easier matching
        message_lower = user_message.lower()
        
        # Check if it's a command help request
        if user_message.startswith("!help"):
            command = user_message.replace("!help", "").strip()
            if command:
                return self.get_command_help(command)
            else:
                return """# Available Commands Help
Use `!help <command>` to get help for specific commands. Example: `!help ls`

## Common Commands
- `ls` - List directory contents
- `cd` - Change directory
- `cat` - Display file contents
- `ssh` - Connect to remote server
- `grep` - Search text patterns

Type `!help` followed by any of these commands for detailed help."""

        # Get level-specific help
        from bandit_levels import BANDIT_LEVELS
        level_info = BANDIT_LEVELS.get(current_level, {})
        
        # Check for different types of queries
        if "objective" in message_lower or "goal" in message_lower:
            return f"""# Level {current_level} Objective

{level_info.get('objective', 'Complete the level challenges.')}

## Description
{level_info.get('description', 'No additional description available.')}"""
            
        elif "hint" in message_lower or "help" in message_lower:
            hints = level_info.get('hints', [])
            if hints:
                return f"""# Level {current_level} Hints

{chr(10).join(['- ' + hint for hint in hints])}

Need more specific help? Try:
- Ask about the level objective
- Use `!help <command>` for command help
- Ask about specific concepts"""
            
        elif any(cmd in message_lower for cmd in self.command_help.keys()):
            # If the message contains a command name, provide help for that command
            for cmd in self.command_help.keys():
                if cmd in message_lower:
                    return self.get_command_help(cmd)
                    
        elif "how" in message_lower:
            return f"""# Level {current_level} Guidance

## Objective
{level_info.get('objective', 'Complete the level challenges.')}

## Useful Commands
{chr(10).join(['- `' + cmd + '`: ' + self.command_help.get(cmd, '') for cmd in level_info.get('useful_commands', [])])}

Need more help? Try:
- Ask for hints
- Use `!help <command>` for detailed command help
- Ask about specific concepts"""

        # If no specific query type is matched, provide a contextual response
        return f"""# Bandit Level {current_level} Assistant

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

What would you like to know about?"""
