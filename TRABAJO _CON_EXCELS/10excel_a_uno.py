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