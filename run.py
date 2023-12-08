import subprocess
import os

def check_and_install(package):
    try:
        __import__(package)
    except ImportError:
        subprocess.run(["pip", "install", package], check=True)

def run_script(script_name):
    python_executable = "python"  # O "python3" dependiendo de tu entorno
    script_path = os.path.join(os.getcwd(), script_name)
    subprocess.run([python_executable, script_path], check=True)

if __name__ == '__main__':
    # Comprobar e instalar dependencias
    for package in ["flask", "pytube"]:
        check_and_install(package)

    # Ejecutar folder_selector.py
    run_script('folder_selector.py')

    # Ejecutar app.py
    run_script('app.py')
