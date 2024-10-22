import unittest
import string
import secrets
from utils.password_generator import PasswordBuilder, PasswordGenerator  # Replace with your actual module name.

class TestPasswordBuilder(unittest.TestCase):
    
    def test_invalid_initialization_length(self):
        """Verifies that a ValueError is raised if length is less than or equal to 0."""
        with self.assertRaises(ValueError) as context:
            PasswordBuilder(0)
        self.assertEqual(str(context.exception), "La longitud de la contraseña debe ser mayor que 0.")

    def test_add_lowercase(self):
        """Verifies that lowercase characters are added correctly."""
        builder = PasswordBuilder(8).add_lowercase()
        self.assertIn('a', builder.character_set)  # Check if lowercase letters are present.
        self.assertEqual(len(builder.forced_chars), 1)  # There should be one forced character.

    def test_add_uppercase(self):
        """Verifies that uppercase characters are added correctly."""
        builder = PasswordBuilder(8).add_uppercase()
        self.assertIn('A', builder.character_set)  # Check if uppercase letters are present.
        self.assertEqual(len(builder.forced_chars), 1)  # There should be one forced character.

    def test_add_numbers(self):
        """Verifies that digits are added correctly."""
        builder = PasswordBuilder(8).add_numbers()
        self.assertIn('0', builder.character_set)  # Check if digits are present.
        self.assertEqual(len(builder.forced_chars), 1)  # There should be one forced character.

    def test_add_symbols(self):
        """Verifies that symbols are added correctly."""
        builder = PasswordBuilder(8).add_symbols()
        self.assertIn('!', builder.character_set)  # Check if symbols are present.
        self.assertEqual(len(builder.forced_chars), 1)  # There should be one forced character.

    def test_build_without_characters(self):
        """Verifies that a ValueError is raised if no characters are selected."""
        builder = PasswordBuilder(8)
        with self.assertRaises(ValueError) as context:
            builder.build()
        self.assertEqual(str(context.exception), "Debe seleccionar al menos un tipo de caracteres.")

    def test_build_with_characters(self):
        """Verifies that a valid password is generated with forced characters."""
        builder = PasswordBuilder(8).add_lowercase().add_uppercase().add_numbers().add_symbols()
        password = builder.build()
        self.assertEqual(len(password), 8)  # Correct length.
        self.assertTrue(any(c.islower() for c in password))  # At least one lowercase.
        self.assertTrue(any(c.isupper() for c in password))  # At least one uppercase.
        self.assertTrue(any(c.isdigit() for c in password))  # At least one digit.
        self.assertTrue(any(c in string.punctuation for c in password))  # At least one symbol.

    def test_build_with_excessive_forced_characters(self):
        """Verifies that a password is constructed even if there are more forced characters than length."""
        builder = PasswordBuilder(4).add_lowercase().add_uppercase()
        builder.forced_chars = ['a', 'B', 'c', 'D', '1']  # Forcing more characters than needed.
        password = builder.build()
        self.assertEqual(len(password), 4)  # Should truncate password to specified length.
        self.assertTrue(all(c in builder.character_set for c in password))  # All chars must be in the set.

class TestPasswordGenerator(unittest.TestCase):
    
    def test_generate_with_all_options(self):
        """Verifies that a password is generated with all options enabled."""
        password = PasswordGenerator.generate(12, True, True, True, True)
        self.assertEqual(len(password), 12)  # Correct length.
        self.assertTrue(any(c.islower() for c in password))  # At least one lowercase.
        self.assertTrue(any(c.isupper() for c in password))  # At least one uppercase.
        self.assertTrue(any(c.isdigit() for c in password))  # At least one digit.
        self.assertTrue(any(c in string.punctuation for c in password))  # At least one symbol.

    def test_generate_without_symbols(self):
        """Verifies that a password is generated without symbols."""
        password = PasswordGenerator.generate(12, False, True, True, True)
        self.assertEqual(len(password), 12)  # Correct length.
        self.assertTrue(any(c.islower() for c in password))  # At least one lowercase.
        self.assertTrue(any(c.isupper() for c in password))  # At least one uppercase.
        self.assertTrue(any(c.isdigit() for c in password))  # At least one digit.
        self.assertFalse(any(c in string.punctuation for c in password))  # No symbols.

    def test_generate_without_numbers(self):
        """Verifies that a password is generated without numbers."""
        password = PasswordGenerator.generate(12, True, False, True, True)
        self.assertEqual(len(password), 12)  # Correct length.
        self.assertTrue(any(c.islower() for c in password))  # At least one lowercase.
        self.assertTrue(any(c.isupper() for c in password))  # At least one uppercase.
        self.assertFalse(any(c.isdigit() for c in password))  # No numbers.
        self.assertTrue(any(c in string.punctuation for c in password))  # At least one symbol.

    def test_generate_without_uppercase(self):
        """Verifies that a password is generated without uppercase letters."""
        password = PasswordGenerator.generate(12, True, True, False, True)
        self.assertEqual(len(password), 12)  # Correct length.
        self.assertTrue(any(c.islower() for c in password))  # At least one lowercase.
        self.assertFalse(any(c.isupper() for c in password))  # No uppercase.
        self.assertTrue(any(c.isdigit() for c in password))  # At least one digit.
        self.assertTrue(any(c in string.punctuation for c in password))  # At least one symbol.

    def test_generate_without_lowercase(self):
        """Verifies that a password is generated without lowercase letters."""
        password = PasswordGenerator.generate(12, True, True, True, False)
        self.assertEqual(len(password), 12)  # Correct length.
        self.assertFalse(any(c.islower() for c in password))  # No lowercase.
        self.assertTrue(any(c.isupper() for c in password))  # At least one uppercase.
        self.assertTrue(any(c.isdigit() for c in password))  # At least one digit.
        self.assertTrue(any(c in string.punctuation for c in password))  # At least one symbol.

if __name__ == "__main__":
    unittest.main()
