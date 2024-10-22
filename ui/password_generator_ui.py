import customtkinter as ctk
from ui.ui_factory import UIFactory
from ui.clipboard_manager import ClipboardManager
from utils.password_generator import PasswordGenerator
from utils.config import UIConfig, UIColors, MessageColors
from typing import List, Tuple

class PasswordGeneratorUI:
    """Interfaz de usuario principal para el generador de contraseñas."""

    def __init__(self):
        self._setup_window()
        self._init_variables()
        self._create_ui()
        self.clipboard_manager = ClipboardManager(self.window)
        self.password_generator = PasswordGenerator()
        
    def _setup_window(self) -> None:
        """Configura la ventana principal."""
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")
        
        self.window = ctk.CTk()
        self.window.title("Generador de Contraseñas")
        self.window.geometry(UIConfig.WINDOW_SIZE)
        self.window.resizable(False, False)

    def _init_variables(self) -> None:
        """Inicializa las variables de control."""
        self.length_var = ctk.IntVar(value=UIConfig.DEFAULT_PASSWORD_LENGTH)
        self.symbols_var = ctk.BooleanVar(value=True)
        self.numbers_var = ctk.BooleanVar(value=True)
        self.uppercase_var = ctk.BooleanVar(value=True)
        self.lowercase_var = ctk.BooleanVar(value=True)
        self.current_password = ""

    def _create_ui(self) -> None:
        """Crea todos los elementos de la interfaz de usuario."""
        self.main_frame = self._create_main_frame()
        self._create_header()
        self.card = self._create_card()
        self._create_length_section()
        self._create_options_section()
        self._create_result_section()

    def _create_main_frame(self) -> ctk.CTkFrame:
        """Crea el frame principal."""
        frame = ctk.CTkFrame(self.window, fg_color=UIColors.TRANSPARENT)
        frame.pack(fill="both", expand=True, padx=UIConfig.PADDING, pady=UIConfig.PADDING)
        return frame

    def _create_header(self) -> None:
        """Crea la sección del encabezado."""
        UIFactory.create_label(
            self.main_frame,
            "Generador de Contraseñas",
            28,
            is_bold=True
        ).pack(pady=(0, 10))
        
        UIFactory.create_label(
            self.main_frame,
            "Crea contraseñas seguras y personalizadas",
            14,
            text_color="gray"
        ).pack(pady=(0, 20))

    def _create_card(self) -> ctk.CTkFrame:
        """Crea la tarjeta principal."""
        card = ctk.CTkFrame(self.main_frame)
        card.pack(fill="both", expand=True, padx=10)
        return card

    def _create_length_section(self) -> None:
        """Crea la sección de longitud de contraseña."""
        length_frame = ctk.CTkFrame(self.card, fg_color=UIColors.TRANSPARENT)
        length_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        self.length_label = UIFactory.create_label(
            length_frame,
            f"Longitud de la contraseña: {self.length_var.get()}",
            14
        )
        self.length_label.pack()
        
        self._create_length_slider()

    def _create_length_slider(self) -> None:
        """Crea el control deslizante para la longitud."""
        ctk.CTkSlider(
            self.card,
            from_=UIConfig.MIN_PASSWORD_LENGTH,
            to=UIConfig.MAX_PASSWORD_LENGTH,
            number_of_steps=UIConfig.MAX_PASSWORD_LENGTH - UIConfig.MIN_PASSWORD_LENGTH,
            variable=self.length_var,
            command=self._update_length_label
        ).pack(padx=20, pady=(0, 20))

    def _create_options_section(self) -> None:
        """Crea la sección de opciones de caracteres."""
        self._create_separator()
        
        UIFactory.create_label(
            self.card,
            "Opciones de caracteres",
            16,
            is_bold=True
        ).pack(pady=(10, 20))
        
        self._create_checkboxes()

    def _create_checkboxes(self) -> None:
        """Crea los checkboxes de opciones."""
        checkbox_options: List[Tuple[ctk.BooleanVar, str]] = [
            (self.symbols_var, "Incluir símbolos (@#$%)"),
            (self.numbers_var, "Incluir números (0-9)"),
            (self.uppercase_var, "Incluir mayúsculas (A-Z)"),
            (self.lowercase_var, "Incluir minúsculas (a-z)")
        ]
        
        for var, text in checkbox_options:
            UIFactory.create_checkbox(self.card, text, var).pack(
                pady=10, padx=20, anchor="w"
            )

    def _create_separator(self) -> None:
        """Crea una línea separadora."""
        separator = ctk.CTkFrame(self.card, height=2, fg_color=UIColors.SEPARATOR)
        separator.pack(fill="x", padx=20, pady=10)

    def _create_result_section(self) -> None:
        """Crea la sección de resultado."""
        result_frame = ctk.CTkFrame(self.card, fg_color=UIColors.TRANSPARENT)
        result_frame.pack(fill="x", padx=20, pady=20)
        
        self._create_password_entry(result_frame)
        self._create_buttons(result_frame)
        
        self.message_label = UIFactory.create_label(self.card, "", 14)
        self.message_label.pack(pady=10)

    def _create_password_entry(self, parent: ctk.CTkFrame) -> None:
        """Crea el campo de entrada para la contraseña."""
        self.password_entry = ctk.CTkEntry(
            parent,
            font=(UIConfig.FONT_FAMILY, 14),
            height=40,
            width=300,
            justify="center"
        )
        self.password_entry.pack(pady=(0, 10))

    def _create_buttons(self, parent: ctk.CTkFrame) -> None:
        """Crea los botones de acción."""
        buttons_frame = ctk.CTkFrame(parent, fg_color=UIColors.TRANSPARENT)
        buttons_frame.pack(fill="x")
        
        ctk.CTkButton(
            buttons_frame,
            text="Generar Contraseña",
            command=self._generate_password,
            font=(UIConfig.FONT_FAMILY, 14, "bold"),
            height=40
        ).pack(side="left", expand=True, padx=5)
        
        ctk.CTkButton(
            buttons_frame,
            text="Copiar",
            command=self._copy_to_clipboard,
            font=(UIConfig.FONT_FAMILY, 14),
            height=40,
            fg_color=UIColors.COPY_BUTTON,
            hover_color=UIColors.COPY_BUTTON_HOVER
        ).pack(side="left", expand=True, padx=5)

    def _update_length_label(self, _: float) -> None:
        """Actualiza la etiqueta de longitud."""
        self.length_label.configure(
            text=f"Longitud de la contraseña: {self.length_var.get()}"
        )

    def _generate_password(self) -> None:
        """Genera una nueva contraseña."""
        try:
            self.current_password = self.password_generator.generate(
                self.length_var.get(),
                self.symbols_var.get(),
                self.numbers_var.get(),
                self.uppercase_var.get(),
                self.lowercase_var.get()
            )
            self.password_entry.delete(0, "end")
            self.password_entry.insert(0, self.current_password)
            self._show_message("¡Contraseña generada exitosamente!", MessageColors.SUCCESS)
        except ValueError as e:
            self._show_message(str(e), MessageColors.ERROR)
        except Exception as e:
            self._show_message(f"Error inesperado: {str(e)}", MessageColors.ERROR)

    def _copy_to_clipboard(self) -> None:
        """Copia la contraseña al portapapeles."""
        password = self.password_entry.get()
        try:
            if password:
                self.clipboard_manager.copy_text(password)
                self._show_message("¡Contraseña copiada al portapapeles!", MessageColors.SUCCESS)
            else:
                self._show_message("No hay contraseña para copiar", MessageColors.WARNING)
        except Exception as e:
            self._show_message(f"Error al copiar: {str(e)}", MessageColors.ERROR)

    def _show_message(self, message: str, color: str) -> None:
        """Muestra un mensaje en la interfaz."""
        self.message_label.configure(text=message, text_color=color)

    def run(self) -> None:
        """Inicia la aplicación."""
        self.window.mainloop()
