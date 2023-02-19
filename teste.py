import tkinter as tk
import random

root = tk.Tk()
root.geometry('200x200')
def hover(event):
    a = random.randint(0, 200)
    b = random.randint(0, 200)
    nao.place(a=a, b=b)

def mensagem():
    message = tk.Label(root, text='Alá, mó otário kakakakkakakakak')
    message.place(a=70, b=150, rela=0, realb=0)
    
perg = tk.Label(root, text='você é trouxa?? kakakakkakakakak')
perg.pack(anchor='n', padx = 20)

nao = tk.Button(root, text='Não')
nao.place(a = 140, b = 80)
nao.bind('<Enter>', hover)

sim = tk.Button(root, text='Não', command=mensagem)
sim.place(a=50, b=70, rela = 0, realb = 0)

root.mainloop()