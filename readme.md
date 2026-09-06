# Python en 5 Líneas 🐍

Scripts cortos que te ahorran horas. Sin librerías externas, sin pedir rutas raras.
Del canal **@Pythonen5Lineas**

### 📂 1. Organizar carpetas - `organizar_carpetas.py`

**¿Qué hace?**
Organiza automáticamente la carpeta donde pongas el script. Crea carpetas por tipo (jpg, pdf, zip, etc.) y mueve todo.

**¿Cómo se usa?**
1. Copia `organizar_carpetas.py` DENTRO de la carpeta que quieres organizar (Descargas, Escritorio, una carpeta de prueba)
2. Doble click. Listo.

No pide ruta. Donde está, ahí organiza.

**Código:**
import os
from pathlib import Path
for archivo in Path('.').iterdir():
    if archivo.is_file() and archivo.name != "organizador.py":
        carpeta = Path(archivo.suffix[1:] or 'otros')
        carpeta.mkdir(exist_ok=True)
        archivo.rename(carpeta / archivo.name)
input("Listo!")

### 💾 2. Localizar archivos pesados - `localizar_archivos_pesados.py`

**¿Qué hace?**
Encuentra los 10 archivos más pesados de tu carpeta de Descargas.

**¿Cómo se usa?**
Solo cambia el nombre de la carpeta en la variable `carpeta` si quieres revisar otra. Por defecto revisa Downloads. Doble click.

**Código:**
import os
from pathlib import Path
carpeta = str(Path.home() / "Downloads")
archivos = sorted([(os.path.getsize(os.path.join(r,f)), os.path.join(r,f)) for r,_,fs in os.walk(carpeta) for f in fs], reverse=True)
for tam, ruta in archivos[:10]: print(f"{tam/1024/1024:.1f} MB - {os.path.basename(ruta)}")

### 📄 Video #3 - 100 JPG → 1 PDF en 5 líneas
from PIL import Image
from pathlib import Path

> Convierte 100 imágenes JPG a un solo PDF en 2 segundos con 5 líneas de Python. Sin páginas con virus ni marcas de agua.

**Instalación:**
```bash
pip install pillow

### ▶️ Requisitos
- Tener Python instalado (python.org)

Hecho por Pythonen5Líneas | github.com/reyesrosdel83
