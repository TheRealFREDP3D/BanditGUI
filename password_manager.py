import json
import os
from pathlib import Path

class PasswordManager:
    def __init__(self):
        self.passwords_file = "user_progress.json"
        self.known_passwords = self._load_passwords()
        
        # Known password for level 0
        self.known_passwords.setdefault('bandit0', 'bandit0')
        self._save_passwords()

    def _load_passwords(self):
        """Load saved passwords from file"""
        try:
            if os.path.exists(self.passwords_file):
                with open(self.passwords_file, 'r') as f:
                    return json.load(f)
        except Exception as e:
            print(f"Error loading passwords: {e}")
        return {}

    def _save_passwords(self):
        """Save passwords to file"""
        try:
            with open(self.passwords_file, 'w') as f:
                json.dump(self.known_passwords, f, indent=4)
        except Exception as e:
            print(f"Error saving passwords: {e}")

    def check_output_for_password(self, level: int, output: str) -> tuple[bool, str]:
        """
        Check if the output contains a valid password for the next level.
        Returns (is_password_found, password if found else '')
        """
        # Clean the output
        output = output.strip()
        
        # If output is exactly 32 characters long, it might be a password
        if len(output) == 32 and all(c in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' for c in output):
            next_level = f'bandit{level + 1}'
            self.known_passwords[next_level] = output
            self._save_passwords()
            return True, output
            
        return False, ''

    def get_password(self, level: int) -> str:
        """Get password for a specific level"""
        return self.known_passwords.get(f'bandit{level}', '')

    def has_completed_level(self, level: int) -> bool:
        """Check if user has completed a specific level"""
        return f'bandit{level + 1}' in self.known_passwords

    def get_progress(self) -> dict:
        """Get user's progress (completed levels)"""
        return {
            'completed_levels': [
                int(k.replace('bandit', '')) - 1 
                for k in self.known_passwords.keys() 
                if k != 'bandit0'
            ],
            'highest_level': max([
                int(k.replace('bandit', '')) 
                for k in self.known_passwords.keys()
            ] + [0])
        }
