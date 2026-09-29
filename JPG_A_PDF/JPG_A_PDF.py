from PIL import Image
from pathlib import Path
imagenes = [Image.open(f).convert("RGB") for f in Path('.').glob('*.jpg')]
imagenes[0].save("documento.pdf", save_all=True, append_images=imagenes[1:])
print("PDF creado!")