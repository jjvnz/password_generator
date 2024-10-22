import customtkinter as ctk

class ClipboardManager:
    """Gestiona las operaciones del portapapeles."""
    
    def __init__(self, window: ctk.CTk):
        self.window = window
    
    def copy_text(self, text: str) -> None:
        """Copia el texto al portapapeles."""
        self.window.clipboard_clear()
        self.window.clipboard_append(text)
        self.window.update()
