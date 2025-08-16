#!/usr/bin/env python3
"""
Startup script para huggingface_mcp_server
Generado automáticamente por QuantFlow-X MCP Environment Injector
"""

import os
from pathlib import Path


def setup_environment():
    """Configurar variables de entorno para huggingface_mcp_server."""
    env_vars = {}

    # Cargar .env si alguna variable falta
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent.parent / '.env')
    for key in list(env_vars.keys()):
        if key not in os.environ and key in env_vars:
            os.environ[key] = str(env_vars[key])

    for key, value in env_vars.items():
        if not os.environ.get(key):
            os.environ[key] = str(value)
        print(f"Set {key} = {'*' * len(os.environ.get(key, ''))}")

    # Configurar PYTHONPATH
    mcp_path = str(Path(__file__).parent.parent.absolute())
    current_pythonpath = os.environ.get('PYTHONPATH', '')
    if mcp_path not in current_pythonpath:
        if current_pythonpath:
            os.environ['PYTHONPATH'] = f"{mcp_path};{current_pythonpath}"
        else:
            os.environ['PYTHONPATH'] = mcp_path
        print(f"Updated PYTHONPATH: {os.environ['PYTHONPATH']}")

def main():
    """Función principal de inicio."""
    print("Iniciando huggingface_mcp_server...")
    setup_environment()

    if not os.environ.get('HF_TOKEN'):
        print("ADVERTENCIA: HF_TOKEN no está configurado. Configure HF_TOKEN en el archivo .env ubicado en la carpeta MCP.")

    # Aquí iría la lógica específica de inicio del servidor
    # Por ahora solo configuramos el entorno
    print("huggingface_mcp_server configurado correctamente.")
    print("Variables de entorno configuradas:")
    for key in ['HF_TOKEN']:
        print(f"  {key}: {'*' * len(os.environ.get(key, '')) if os.environ.get(key) else 'NOT SET'}")

if __name__ == "__main__":
    main()
