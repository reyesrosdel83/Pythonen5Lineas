from pathlib import Path
import hashlib

def hash_file(p): return hashlib.md5(p.read_bytes()).hexdigest()
visto = {}
for f in Path.home().joinpath("Downloads").glob("*.*"):
    h = hash_file(f)
    print(f"DUPLICADO: {f.name}") if h in visto else visto.update({h: f})