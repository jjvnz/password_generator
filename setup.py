from cx_Freeze import setup, Executable

# Opciones de construcción
build_exe_options = {
    "packages": ["customtkinter", "ui", "utils"],  # Agrega las bibliotecas necesarias
    "include_files": [],  # Agrega archivos adicionales si es necesario
}

# Información del paquete
setup(
    name="Generador de Contraseñas Seguras",
    version="0.1",
    description="Aplicación para generar contraseñas seguras",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base="Win32GUI")],  # Cambia a "Console" si usas la consola
)
