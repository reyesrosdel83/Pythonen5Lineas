import tkinter as tk, datetime as dt
w = tk.Tk(); w.geometry("320x180"); w.eval('tk::PlaceWindow . center')
n=tk.Entry(w, justify="center"); a=tk.Entry(w, justify="center"); t=tk.Label(w, font=("Arial", 13, "bold")); [x.pack(pady=4) for x in (n,a,t)]
n.insert(0, "Tu nombre"); a.insert(0, "2000")
tk.Button(w, text="Ver edad", command=lambda: t.config(text=f"{n.get()}, tienes {dt.date.today().year-int(a.get())}")).pack(pady=5)
w.mainloop()