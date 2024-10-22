from dataclasses import dataclass

@dataclass
class UIConfig:
    """Configuración de la interfaz de usuario."""
    WINDOW_SIZE: str = "500x650"
    FONT_FAMILY: str = "Helvetica Neue"
    DEFAULT_PASSWORD_LENGTH: int = 12
    MIN_PASSWORD_LENGTH: int = 4
    MAX_PASSWORD_LENGTH: int = 32
    PADDING: int = 20

@dataclass
class UIColors:
    """Colores utilizados en la interfaz."""
    TRANSPARENT: str = "transparent"
    SEPARATOR: str = "gray70"
    COPY_BUTTON: str = "gray40"
    COPY_BUTTON_HOVER: str = "gray30"

@dataclass
class MessageColors:
    """Colores para los mensajes de estado."""
    SUCCESS: str = "green"
    ERROR: str = "red"
    WARNING: str = "orange"
