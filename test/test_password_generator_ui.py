import unittest
from unittest.mock import patch, MagicMock
from ui.password_generator_ui import PasswordGeneratorUI  # Ensure this import is correct


class TestPasswordGeneratorUI(unittest.TestCase):
    def setUp(self):
        """Set up the environment before each test."""
        self.ui = PasswordGeneratorUI()
        self.ui.window = MagicMock()  # Mock the window to avoid opening the GUI

    def test_initialization(self):
        """Test the initialization of the UI."""
        self.assertIsNotNone(self.ui.length_var)
        self.assertEqual(self.ui.length_var.get(), 12)  # Check the expected default value

    def test_update_length_label(self):
        """Test that the length label updates correctly."""
        self.ui.length_var.set(16)
        self.ui.update_length_label(0)
        self.assertEqual(self.ui.length_label.cget("text"), "Longitud de la contraseña: 16")

    @patch('utils.password_generator.PasswordGenerator.generate')
    def test_generate_password(self, mock_generate):
        """Test password generation functionality."""
        mock_generate.return_value = "TestPassword123!"
        self.ui.password_generator.generate = mock_generate

        self.ui.length_var.set(16)
        self.ui.symbols_var.set(True)
        self.ui.numbers_var.set(True)
        self.ui.uppercase_var.set(True)
        self.ui.lowercase_var.set(True)

        self.ui.generate_password_command.execute()  # Call the command
        self.assertEqual(self.ui.password_entry.get(), "TestPassword123!")
        self.assertEqual(self.ui.message_label.cget("text"), "¡Contraseña generada exitosamente!")

    @patch('ui.clipboard_manager.ClipboardManager.copy_text')
    def test_copy_to_clipboard(self, mock_copy_text):
        """Test the copy to clipboard functionality."""
        self.ui.password_entry.insert(0, "TestPassword123!")
        
        self.ui.copy_to_clipboard_command.execute()  # Call the command
        mock_copy_text.assert_called_once_with("TestPassword123!")
        self.assertEqual(self.ui.message_label.cget("text"), "¡Contraseña copiada al portapapeles!")

    def test_copy_no_password(self):
        """Test attempting to copy without a password."""
        self.ui.password_entry.delete(0, "end")
        
        self.ui.copy_to_clipboard_command.execute()  # Call the command
        self.assertEqual(self.ui.message_label.cget("text"), "No hay contraseña para copiar")


if __name__ == "__main__":
    unittest.main()
