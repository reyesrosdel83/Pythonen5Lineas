import pandas as pd
import random

productos = ["Laptop HP 15\"", "Mouse Logitech", "Teclado Mecánico", "Monitor 24\" Samsung", "Audífonos Sony", "Silla Gamer", "Webcam HD", "SSD 1TB", "RAM 16GB", "Impresora Epson"]

for mes in ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre"]:
    datos = []
    for p in productos:
        datos.append([p, random.randint(5, 150), round(random.uniform(10, 800), 2)])
    
    df = pd.DataFrame(datos, columns=["Producto", "Inventario", "Precio"])
    df.to_excel(f"{mes}.xlsx", index=False)

print("¡10 excels creados!")