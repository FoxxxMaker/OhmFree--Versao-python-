import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mb
import Back as bk

app = tk.Tk()
app.title("OhmFree")
app.geometry("800x500")

lbl = tk.Label(app, text="Bem-vindo!")
lbl.pack(pady=20)

lbl2 = tk.Label(app, text="Cores: preto: 0, marrom: 1, vermelho: 2, laranja: 3, amarelo: 4, verde: 5, azul: 6, violeta: 7, cinza: 8, branco: 9")
lbl2.pack(pady=11)

lbl3 = tk.Label(app, text="Insira a primeira cor.")
lbl3.pack(pady=10)

lista = ttk.Combobox(app, values=tuple(bk.cores.keys()))
lista.pack(pady=10)

lbl4 = tk.Label(app, text="Insira a segunda cor.")
lbl4.pack(pady=10)

Lista2 = ttk.Combobox(app, values=tuple(bk.cores.keys()))
Lista2.pack(pady=10)

lbl5 = tk.Label(app, text="Insira a terceira cor.")
lbl5.pack(pady=10)

Lista3 = ttk.Combobox(app, values=tuple(bk.cores.keys()))
Lista3.pack(pady=10)

app.mainloop()