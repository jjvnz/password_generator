import customtkinter as ctk
from customtkinter import CTkLabel, CTkCheckBox

class UIFactory:
    """Fábrica para crear elementos de la interfaz de usuario."""
    
    @staticmethod
    def create_label(parent, text, font_size, is_bold=False, text_color=None):
        """Crea una etiqueta con el estilo especificado."""
        weight = "bold" if is_bold else "normal"
        return CTkLabel(
            parent,
            text=text,
            font=("Helvetica Neue", font_size, weight),
            text_color=text_color
        )
    
    @staticmethod
    def create_checkbox(parent, text, variable):
        """Crea un checkbox con el estilo especificado."""
        return CTkCheckBox(
            parent,
            text=text,
            variable=variable,
            font=("Helvetica Neue", 14),
            checkbox_height=24,
            checkbox_width=24
        )
