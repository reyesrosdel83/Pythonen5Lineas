import os
from pypdf import PdfMerger

merger = PdfMerger()
pdfs = [f for f in os.listdir() if f.lower().endswith(".pdf")]

# los ordena por nombre para que no salgan desordenados
pdfs.sort()

for pdf in pdfs:
    if pdf != "UNIDOS.pdf": # para no incluirse a sí mismo
        merger.append(pdf)

merger.write("UNIDOS.pdf")
merger.close()

print(f"Listo! Se unieron {len(pdfs)} PDFs en UNIDOS.pdf")