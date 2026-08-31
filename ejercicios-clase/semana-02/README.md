# Semana 02 — Configuración del entorno

Para crear el entorno virtual desde la raíz del repositorio se utiliza `python -m venv venv`.
En Windows PowerShell, el entorno se activa con `.\venv\Scripts\Activate.ps1`.
Una vez activado, se pueden instalar las dependencias necesarias con `pip install -r requirements.txt`.
El archivo `requirements.txt` contiene las versiones exactas de las librerías utilizadas.
Para reproducir el entorno, se debe clonar el repositorio, crear un nuevo entorno virtual y ejecutar el comando de instalación.
El entorno virtual se desactiva utilizando el comando `deactivate`.
La carpeta `venv/` no se incluye en Git porque está registrada en `.gitignore`.