import os
from pathlib import Path
for archivo in Path('.').iterdir():
    if archivo.is_file() and archivo.name != "organizador.py":
        carpeta = Path(archivo.suffix[1:] or 'otros')
        carpeta.mkdir(exist_ok=True)
        archivo.rename(carpeta / archivo.name)
input("Listo!")