import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
import pandas as pd

def seleccionar_carpeta():
    carpeta = filedialog.askdirectory(title="Selecciona la carpeta con los Excels")
    if carpeta:
        entry_ruta.delete(0, tk.END)
        entry_ruta.insert(0, carpeta)

def unir_excels():
    ruta_str = entry_ruta.get().strip()
    if not ruta_str:
        messagebox.showwarning("Atención", "Primero selecciona una carpeta")
        return
    ruta = Path(ruta_str)
    archivos = list(ruta.glob("*.xlsx")) + list(ruta.glob("*.xls"))
    archivos = [a for a in archivos if not a.name.startswith("EXCELS_UNIDOS") and not a.name.startswith("TODO_JUNTO") and not a.name.startswith("10_EXCELS")]
    if not archivos:
        messagebox.showerror("Error", "No encontré archivos .xlsx / .xls en esa carpeta")
        return
    label_status.config(text=f"Creando archivo con {len(archivos)} pestañas...")
    ventana.update()
    try:
        salida = ruta / "10_EXCELS_EN_1.xlsx"
        with pd.ExcelWriter(salida, engine='openpyxl') as writer:
            for f in archivos[:10]:
                try:
                    df = pd.read_excel(f)
                    nombre_hoja = f.stem[:31].replace(":","").replace("\\","").replace("/","").replace("?","").replace("*","").replace("[","").replace("]","")
                    if not nombre_hoja:
                        nombre_hoja = f"Hoja_{archivos.index(f)+1}"
                    if df.empty:
                        df = pd.DataFrame([["(archivo vacio)"]])
                    df.to_excel(writer, index=False, sheet_name=nombre_hoja)
                except Exception as e:
                    nombre_hoja = f.stem[:28] + "_ERR"
                    pd.DataFrame([[f"Error: {e}"]]).to_excel(writer, index=False, sheet_name=nombre_hoja[:31])

        messagebox.showinfo("¡Listo!", f"Se creó 1 archivo con {min(len(archivos),10)} pestañas\n\nGuardado en:\n{salida}")
        label_status.config(text=f"¡Hecho! {min(len(archivos),10)} pestañas creadas")
    except Exception as e:
        messagebox.showerror("Error", str(e))
        label_status.config(text="Error")

ventana = tk.Tk()
ventana.title("10 EXCELS EN 1 - 10 PESTAÑAS")
ventana.geometry("500x280")
ventana.resizable(False, False)
ventana.configure(bg="#111")
tk.Label(ventana, text="10 EXCELS EN 1 (10 PESTAÑAS)", bg="#111", fg="#00FF88", font=("Arial", 12, "bold")).pack(pady=15)
tk.Label(ventana, text="Carpeta donde están los Excels:", bg="#111", fg="white", font=("Arial", 10)).pack(anchor="w", padx=20)
frame = tk.Frame(ventana, bg="#111")
frame.pack(pady=5, padx=20, fill="x")
entry_ruta = tk.Entry(frame, font=("Arial", 10), width=38)
entry_ruta.pack(side="left", padx=(0,10))
tk.Button(frame, text="📁 Examinar", command=seleccionar_carpeta, bg="#00FF88", fg="black", font=("Arial", 9, "bold"), width=10).pack(side="left")
tk.Button(ventana, text="CREAR 10 PESTAÑAS AHORA", command=unir_excels, bg="#FF0000", fg="white", font=("Arial", 11, "bold"), height=2, width=25).pack(pady=25)
label_status = tk.Label(ventana, text="Selecciona una carpeta para empezar", bg="#111", fg="#888", font=("Arial", 9))
label_status.pack()
ventana.mainloop()