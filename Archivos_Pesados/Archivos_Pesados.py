import os
from pathlib import Path
carpeta = str(Path.home() / "Downloads")
archivos = sorted([(os.path.getsize(os.path.join(r,f)), os.path.join(r,f)) for r,_,fs in os.walk(carpeta) for f in fs], reverse=True)
for tam, ruta in archivos[:10]: print(f"{tam/1024/1024:.1f} MB - {os.path.basename(ruta)}")