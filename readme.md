Python en 5 Líneas 🐍
Scripts cortos que te ahorran horas. Sin librerías raras, sin pedir rutas. Donde está el script, ahí trabaja.
Del canal @Pythonen5Lineas | GitHub: reyesrosdel183/Pythonen5Lineas

📂 1. Organizar carpetas - organizar_carpetas.py
¿Qué hace?
Organiza automáticamente la carpeta donde pongas el script. Crea carpetas por tipo (jpg, pdf, zip, etc.) y mueve todo.

¿Cómo se usa?

Copia organizar_carpetas.py DENTRO de la carpeta que quieres organizar (Descargas, Escritorio, etc.)
Doble click. Listo.
Código:

python
import os
from pathlib import Path
for archivo in Path('.').iterdir():
    if archivo.is_file() and archivo.name != "organizar_carpetas.py":
        carpeta = Path(archivo.suffix[1:] or 'otros')
        carpeta.mkdir(exist_ok=True)
        archivo.rename(carpeta / archivo.name)
input("¡Listo!")
💾 2. Localizar archivos pesados - Archivos_Pesados.py
¿Qué hace?
Encuentra los 10 archivos más pesados de tu carpeta de Descargas (o la que elijas).

¿Cómo se usa?
Solo cambia Downloads por otra carpeta si quieres. Doble click.

Código:

python
import os
from pathlib import Path
carpeta = str(Path.home() / "Downloads")
archivos = sorted([(os.path.getsize(os.path.join(r,f)), os.path.join(r,f)) for r,_,fs in os.walk(carpeta) for f in fs], reverse=True)
for tam, ruta in archivos[:10]: 
    print(f"{tam/1024/1024:.1f} MB - {os.path.basename(ruta)}")
📄 3. 100 JPG → 1 PDF - JPG_A_PDF.py
Convierte 100 imágenes JPG a un solo PDF en 2 segundos. Sin páginas con virus ni marcas de agua.

Instalación:

bash
pip install pillow
Código:

python
from PIL import Image
from pathlib import Path
imagenes = [Image.open(f).convert('RGB') for f in Path('.').glob('*.jpg')]
imagenes[0].save('TODO.pdf', save_all=True, append_images=imagenes[1:])
📊 4. Unir 10 Excels en 1 - 10excel_a_uno.py [NUEVO]
¿Qué hace?
Pasa de una carpeta así: 10 archivos Enero.xlsx, Febrero.xlsx... a ESTO: 1 solo archivo TODO_JUNTO.xlsx con 10 hojas, cada una con el nombre del archivo.

¿Cómo se usa?

Copia 10excel_a_uno.py DENTRO de la carpeta donde están tus 10 excels
Doble click. Te crea TODO_JUNTO.xlsx en la misma carpeta.
Instalación:

bash
pip install pandas openpyxl
Código completo (8 líneas):

python
import pandas as pd, glob, os

archivos = glob.glob("*.xlsx")

with pd.ExcelWriter("TODO_JUNTO.xlsx") as writer:
    for archivo in archivos:
        if "TODO_JUNTO" in archivo:
            continue
        nombre_hoja = os.path.splitext(os.path.basename(archivo))[0][:31]
        df = pd.read_excel(archivo)
        df.to_excel(writer, sheet_name=nombre_hoja, index=False)

print("¡Listo!")
¿Por qué funciona?

if "TODO_JUNTO" in archivo: continue evita que el script se lea a sí mismo en bucle.
[:31] porque Excel no permite nombres de hoja con más de 31 caracteres.
▶ Requisitos generales
Tener Python instalado desde python.org
Para cada script instalar solo lo que dice en Instalación
Hecho con ❤️ por Python en 5 Líneas | youtube.com/@Pythonen5Lineas
