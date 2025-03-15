import secrets
import string

class PasswordGenerator:
    def __init__(self, length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
        """
        Initialize the PasswordGenerator with user preferences.
        
        :param length: Length of the password (default: 12).
        :param use_uppercase: Include uppercase letters (default: True).
        :param use_lowercase: Include lowercase letters (default: True).
        :param use_digits: Include digits (default: True).
        :param use_special: Include special characters (default: True).
        """
        self.length = length
        self.use_uppercase = use_uppercase
        self.use_lowercase = use_lowercase
        self.use_digits = use_digits
        self.use_special = use_special

    def validate_input(self):
        """
        Validate the user's input to ensure it meets the requirements.
        
        :return: True if input is valid, False otherwise.
        """
        if self.length < 8 or self.length > 64:
            return False
        if not (self.use_uppercase or self.use_lowercase or self.use_digits or self.use_special):
            return False
        return True

    def generate_password(self):
        """
        Generate a cryptographically secure password based on user preferences.
        
        :return: Generated password as a string.
        """
        characters = ""
        if self.use_uppercase:
            characters += string.ascii_uppercase
        if self.use_lowercase:
            characters += string.ascii_lowercase
        if self.use_digits:
            characters += string.digits
        if self.use_special:
            characters += string.punctuation

        if not characters:
            raise ValueError("At least one character set must be selected.")

        password = ''.join(secrets.choice(characters) for _ in range(self.length))
        return password