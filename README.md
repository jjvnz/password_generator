# Generador de Contraseñas Seguras

## Descripción

Aplicación en Python que genera contraseñas aleatorias y seguras utilizando `customtkinter` para una interfaz gráfica amigable.

## Características

- **Generación de Contraseñas**: Crea contraseñas aleatorias.
- **Personalización**: Ajusta la longitud y selecciona tipos de caracteres (mayúsculas, minúsculas, números, símbolos).
- **Interfaz Intuitiva**: Experiencia de usuario sencilla.
- **Función de Copiado**: Copia contraseñas al portapapeles con un clic.

## Requisitos del Sistema

- **Miniconda**: [Descargar Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- **Python**: Versión 3.13 o superior.
- **Dependencias**:
  - `customtkinter==5.2.2`
  - `darkdetect==0.8.0`
  - `packaging==24.1`
  - `cx_Freeze`

## Instalación

### 1. Clonar el Repositorio

```bash
git clone https://github.com/jjvnz/password_generator.git
cd password_generator
```

### 2. Crear un Entorno Virtual

**Conda:**

```bash
conda create -n password_generator python=3.13
conda activate password_generator
```

**O** 

**Pip (sin conda):**

```bash
python -m venv password_generator
source password_generator/bin/activate  # En Linux/Mac
.\password_generator\Scripts\activate   # En Windows
```

### 3. Instalar Dependencias

**Conda:**

```bash
conda install --file requirements.txt
```

**O** 

**Pip:**

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la Aplicación

```bash
python main.py
```

## Uso

1. **Seleccionar Longitud**.
2. **Elegir Tipos de Caracteres**.
3. **Generar Contraseña**.
4. **Copiar al Portapapeles**.

## Contribuciones

1. Haz un fork del repositorio.
2. Crea una nueva rama para cambios (`git checkout -b feature/nueva-funcionalidad`).
3. Haz commit (`git commit -m 'Añadir nueva funcionalidad'`).
4. Envía un pull request.

## Licencia

Proyecto bajo la [Licencia MIT](LICENSE).