import pandas as pd, re
from pathlib import Path

df = pd.read_excel("clientes.xlsx")
base = Path("Clientes_2024")
SUB = ["01_Facturas", "02_Contratos", "03_Entregables", "04_Comunicacion"]
limpiar = lambda n: re.sub(r'[\\/*?:"<>|]', "_", str(n)).strip()

for _, f in df.iterrows():
    if pd.isna(f["Cliente"]): continue
    c, p = limpiar(f["Cliente"]), limpiar(f.get("Proyecto", ""))
    ruta = base / c / p if p else base / c
    for s in SUB: (ruta / s).mkdir(parents=True, exist_ok=True)

print(f"Listo Rosdel. {len(df)} clientes en {base.resolve()}")