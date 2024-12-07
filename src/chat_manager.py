import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

class ChatManager:
    def __init__(self):
        """Initialize the ChatManager"""
        self.api_key = os.getenv('GITHUB_API_KEY')
        self.base_url = "https://models.inference.ai.azure.com"
        self.model = "Meta-Llama-3.1-70B-Instruct"
        self.current_level = None
        self.bandit_levels = {}  # Will be set from app.py
        self.hint_index = {}  # Track which hint each user has seen
        self.solve_attempts = {}  # Track solve attempts per level
        self.used_quotes = {}  # Track used quotes per level
        self.solve_quotes = []  # Regular quotes
        self.solve_quotes_nasty = []  # Quotes for repeat attempts
        self.solve_response = ""  # Response template
        
        # Load solve quotes and response template
        try:
            with open(os.path.join(os.path.dirname(__file__), 'templates', 'solve_quotes.txt'), 'r', encoding='utf-8') as f:
                self.solve_quotes = [line.strip() for line in f if line.strip()]
        except Exception as e:
            print(f"Error loading solve quotes: {e}")
            
        try:
            with open(os.path.join(os.path.dirname(__file__), 'templates', 'solve_quotes_nasty.txt'), 'r', encoding='utf-8') as f:
                self.solve_quotes_nasty = [line.strip() for line in f if line.strip()]
        except Exception as e:
            print(f"Error loading nasty solve quotes: {e}")
            
        try:
            with open(os.path.join(os.path.dirname(__file__), 'templates', 'solve_response.txt'), 'r', encoding='utf-8') as f:
                self.solve_response = f.read()
        except Exception as e:
            print(f"Error loading solve response: {e}")
        
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

    def set_bandit_levels(self, levels):
        """Set the bandit levels data from app.py"""
        self.bandit_levels = levels

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
            "ls": """```python
# List files in current directory
ls

# List all files (including hidden)
ls -la

# List files with human-readable sizes
ls -lh
```""",
            "cd": """```python
# Go to home directory
cd ~

# Go up one directory
cd ..

# Go to specific directory
cd /path/to/directory
```""",
            "cat": """```python
# Display file contents
cat filename

# Display file with line numbers
cat -n filename

# Display multiple files
cat file1 file2
```""",
            "ssh": """```python
# Connect to remote server
ssh username@hostname

# Connect on specific port
ssh -p 2220 username@hostname

# Use specific key file
ssh -i keyfile username@hostname
```"""
        }
        return examples.get(command, "```\n# Basic usage\n" + command + "\n`")

    def get_next_hint(self):
        """Get the next available hint for the current level"""
        level_info = self.bandit_levels.get(str(self.current_level), {})
        hints = level_info.get('hints', [])
        
        if not hints:
            return "No hints available for this level."
            
        # Initialize hint index for this level if not exists
        if self.current_level not in self.hint_index:
            self.hint_index[self.current_level] = 0
            
        # Get current hint index
        current_index = self.hint_index[self.current_level]
        
        # If we've shown all hints, return a message
        if current_index >= len(hints):
            return f"You've seen all {len(hints)} hints for this level. Try solving the challenge or ask for specific help!"
            
        # Get the next hint and increment the counter
        hint = hints[current_index]
        self.hint_index[self.current_level] += 1
        
        return f"""# Hint {current_index + 1} of {len(hints)}

{hint}

Type `!hint` again for the next hint."""

    def get_solve_response(self):
        """Get a response for the !solve command"""
        # Initialize solve attempts and used quotes for this level if not exists
        if self.current_level not in self.solve_attempts:
            self.solve_attempts[self.current_level] = 0
            self.used_quotes[self.current_level] = set()

        # Get current attempt number
        current_attempts = self.solve_attempts[self.current_level]
        
        # Prepare response based on attempt number
        if current_attempts == 0:
            # First attempt - use regular quotes
            if not self.solve_quotes:
                quote = "Nice try, but I won't give you the answer! Try using !hint instead."
            else:
                import random
                available_quotes = [q for q in self.solve_quotes if q not in self.used_quotes[self.current_level]]
                if not available_quotes:  # If all quotes used, reset the used quotes
                    self.used_quotes[self.current_level].clear()
                    available_quotes = self.solve_quotes
                quote = random.choice(available_quotes)
                self.used_quotes[self.current_level].add(quote)
        elif current_attempts == 1:
            # Second attempt - use special response
            quote = """<div style="font-size: 24px; color: #FF6B6B; text-align: center; padding: 20px; border-left: 4px solid #FF6B6B;">
Hmm... trying to get the answer again? 🤔

I admire your persistence, but maybe try:
1. Using the `!hint` command
2. Breaking down the problem
3. Learning the commands properly

Remember: Mastery comes through practice, not shortcuts! 💪
</div>"""
        else:
            # Third attempt and beyond - use nasty quotes
            if not self.solve_quotes_nasty:
                quote = "Still trying? The answer is still no! Try !hint instead."
            else:
                import random
                available_quotes = [q for q in self.solve_quotes_nasty if q not in self.used_quotes[self.current_level]]
                if not available_quotes:  # If all quotes used, reset the used quotes
                    self.used_quotes[self.current_level].clear()
                    available_quotes = self.solve_quotes_nasty
                quote = random.choice(available_quotes)
                self.used_quotes[self.current_level].add(quote)
        
        # Increment the attempt counter
        self.solve_attempts[self.current_level] += 1
        
        # Return the formatted response
        if self.solve_response and current_attempts != 1:  # Don't use template for second attempt
            return self.solve_response.replace('[QUOTE]', quote)
        else:
            return quote

    def generate_response(self, user_message, current_level=0):
        """Generate a response based on user message"""
        # Update current level
        self.current_level = current_level
        
        # Convert message to lowercase for easier matching
        message_lower = user_message.lower()
        
        # Check if it's a solve attempt
        if message_lower.startswith("!solve"):
            return self.get_solve_response()
            
        # Check if it's a level info request
        if message_lower.startswith("!level"):
            level_info = self.bandit_levels.get(str(self.current_level), {})
            return f"""# Level {self.current_level} Information

## Description
{level_info.get('description', 'No description available.')}

## Objective
{level_info.get('objective', 'No objective available.')}

## Useful Commands
{chr(10).join(['- `' + cmd + '`' for cmd in level_info.get('useful_commands', [])])}

Type `!hint` to get hints for this level."""

        # Check if it's a hint request
        if message_lower.startswith("!hint"):
            return self.get_next_hint()

        # Check if it's a command help request
        if user_message.startswith("!help"):
            command = user_message.replace("!help", "").strip()
            if command:
                return self.get_command_help(command)
            else:
                return """# Available Commands Help
Use `!help <command>` to get help for specific commands.

## Chat Commands
- `!help <command>` - Get detailed help for a command
- `!level` - Display current level info
- `!hint` - Get a hint for the current level
- `!solve` - Get a hint (but not the answer!)

## Common Linux Commands
- `ls` - List directory contents
- `cd` - Change directory
- `cat` - Display file contents
- `ssh` - Connect to remote server
- `grep` - Search text patterns

Type `!help` followed by any command for detailed help and examples."""

        # Get level-specific help
        level_info = self.bandit_levels.get(str(self.current_level), {})
        
        # Check for different types of queries
        if "objective" in message_lower or "goal" in message_lower:
            return f"""# Level {self.current_level} Objective

{level_info.get('objective', 'Complete the level challenges.')}

## Description
{level_info.get('description', 'No additional description available.')}"""
            
        elif "hint" in message_lower or "help" in message_lower:
            return """# Need Help?

Type `!hint` to get a hint for the current level.
Type `!help <command>` to get help for a specific command.
Type `!level` to see the current level information."""

        elif any(cmd in message_lower for cmd in self.command_help.keys()):
            # If the message contains a command name, provide help for that command
            for cmd in self.command_help.keys():
                if cmd in message_lower:
                    return self.get_command_help(cmd)
                    
        elif "how" in message_lower:
            return f"""# Level {self.current_level} Guidance

## Objective
{level_info.get('objective', 'Complete the level challenges.')}

## Useful Commands
{chr(10).join(['- `' + cmd + '`: ' + self.command_help.get(cmd, '') for cmd in level_info.get('useful_commands', [])])}

Need more help? Try:
- Asking for hints
- Using `!help <command>` for detailed command help
- Asking about specific concepts"""

        # If no specific query type is matched, provide a contextual response
        return f"""# Bandit Level {self.current_level} Assistant

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

    def get_response(self, message):
        """Process user message and return appropriate response"""
        try:
            # First try to generate a contextual response
            response = self.generate_response(message)
            if response:
                return response

            # If no specific response is generated, provide a general help message
            return """I'm here to help you learn! Try:
- Asking about specific commands using `!help <command>`
- Getting level information with `!level`
- Asking for hints about the current challenge
- Questions about Linux commands or security concepts"""

        except Exception as e:
            return f"I encountered an error while processing your message: {str(e)}"
