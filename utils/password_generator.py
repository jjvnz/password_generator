import secrets
import string

class PasswordBuilder:
    """Builder para la generación de contraseñas seguras."""

    def __init__(self, length: int):
        if length <= 0:
            raise ValueError("La longitud de la contraseña debe ser mayor que 0.")
        self.length = length
        self.character_set = ""
        self.forced_chars = []

    def add_lowercase(self):
        """Agrega caracteres en minúscula al conjunto."""
        self.character_set += string.ascii_lowercase
        if len(self.forced_chars) < self.length:
            self.forced_chars.append(secrets.choice(string.ascii_lowercase))
        return self

    def add_uppercase(self):
        """Agrega caracteres en mayúscula al conjunto."""
        self.character_set += string.ascii_uppercase
        if len(self.forced_chars) < self.length:
            self.forced_chars.append(secrets.choice(string.ascii_uppercase))
        return self

    def add_numbers(self):
        """Agrega dígitos al conjunto."""
        self.character_set += string.digits
        if len(self.forced_chars) < self.length:
            self.forced_chars.append(secrets.choice(string.digits))
        return self

    def add_symbols(self):
        """Agrega símbolos al conjunto."""
        self.character_set += string.punctuation
        if len(self.forced_chars) < self.length:
            self.forced_chars.append(secrets.choice(string.punctuation))
        return self

    def build(self) -> str:
        """Genera la contraseña con los caracteres especificados."""
        if not self.character_set:
            raise ValueError("Debe seleccionar al menos un tipo de caracteres.")
        
        # Truncar forced_chars si excede la longitud
        password = self.forced_chars[:self.length]  # Asegura que no exceda la longitud especificada
        if len(password) < self.length:
            password += [secrets.choice(self.character_set) for _ in range(self.length - len(password))]
        
        # Mezclar los caracteres para evitar que los forzados estén siempre al inicio
        secrets.SystemRandom().shuffle(password)
        return ''.join(password)

class PasswordGenerator:
    """Generador de contraseñas usando PasswordBuilder."""

    @staticmethod
    def generate(length: int, use_symbols: bool, use_numbers: bool,
                 use_uppercase: bool, use_lowercase: bool) -> str:
        """Genera una contraseña segura según los parámetros especificados."""
        builder = PasswordBuilder(length)
        if use_lowercase:
            builder.add_lowercase()
        if use_uppercase:
            builder.add_uppercase()
        if use_numbers:
            builder.add_numbers()
        if use_symbols:
            builder.add_symbols()

        return builder.build()
