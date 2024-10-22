import secrets
import string

class PasswordGenerator:
    """Clase para generar contraseñas seguras."""
    
    @staticmethod
    def generate(length: int, use_symbols: bool, use_numbers: bool,
                 use_uppercase: bool, use_lowercase: bool) -> str:
        """Genera una contraseña segura según los parámetros especificados."""
        character_set = ""
        if use_lowercase:
            character_set += string.ascii_lowercase
        if use_uppercase:
            character_set += string.ascii_uppercase
        if use_numbers:
            character_set += string.digits
        if use_symbols:
            character_set += string.punctuation
            
        if not character_set:
            raise ValueError("Debe seleccionar al menos un tipo de caracteres")
            
        return ''.join(secrets.choice(character_set) for _ in range(length))
