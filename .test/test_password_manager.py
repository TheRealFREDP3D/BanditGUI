import unittest
from password_manager import PasswordManager


class TestPasswordManager(unittest.TestCase):
    def setUp(self):
        self.password_manager = PasswordManager()

    def test_valid_password(self):
        # Test with a valid password
        level = 0
        valid_password = "A" * 32  # 32-character alphanumeric string
        is_password, password = self.password_manager.check_output_for_password(
            level, valid_password
        )
        self.assertTrue(is_password)
        self.assertEqual(password, valid_password)
        self.assertIn("bandit1", self.password_manager.known_passwords)
        self.assertEqual(
            self.password_manager.known_passwords["bandit1"], valid_password
        )

    def test_invalid_password_length(self):
        # Test with an invalid password due to incorrect length
        level = 0
        invalid_password = "A" * 31  # 31-character string
        is_password, password = self.password_manager.check_output_for_password(
            level, invalid_password
        )
        self.assertFalse(is_password)
        self.assertEqual(password, "")

    def test_invalid_password_characters(self):
        # Test with an invalid password due to non-alphanumeric characters
        level = 0
        invalid_password = (
            "A" * 31 + "!"
        )  # 32-character string with a special character
        is_password, password = self.password_manager.check_output_for_password(
            level, invalid_password
        )
        self.assertFalse(is_password)
        self.assertEqual(password, "")


if __name__ == "__main__":
    unittest.main()
