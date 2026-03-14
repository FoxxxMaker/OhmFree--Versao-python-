import tkinter as tk
import tkinter.messagebox as mb

app = tk.Tk()
app.title("OhmFree")
app.geometry("800x500")

lbl = tk.Label(app, text="Bem-vindo!")
lbl.pack(pady=20)

lbl2 = tk.Label(app, text="Cores: preto: 0, marrom: 1, vermelho: 2, laranja: 3, amarelo: 4, verde: 5, azul: 6, violeta: 7, cinza: 8, branco: 9")
lbl2.pack(pady=11)

lbl3 = tk.Label(app, text="Insira a primeira cor.")
lbl3.pack(pady=10)



app.mainloop()