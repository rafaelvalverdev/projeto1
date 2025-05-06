import tkinter as tk
from tkinter import messagebox
import math


class CalculadoraCientifica:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Científica")
        self.root.geometry("400x500")

        # Campo de entrada
        self.entrada = tk.Entry(root, font=('Arial', 14), justify='right')
        self.entrada.grid(row=0, column=0, columnspan=4,
                          padx=10, pady=10, ipady=10)

        # Botões numéricos e operações básicas
        botoes = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('√', 5, 0), ('sin', 5, 1), ('cos', 5, 2), ('tan', 5, 3),
            ('log', 6, 0), ('π', 6, 1), ('^', 6, 2), ('C', 6, 3)
        ]

        for (texto, linha, coluna) in botoes:
            botao = tk.Button(root, text=texto, font=(
                'Arial', 12), command=lambda t=texto: self.clique(t))
            botao.grid(row=linha, column=coluna, padx=5,
                       pady=5, ipadx=10, ipady=10)

    def clique(self, valor):
        if valor == '=':
            try:
                expressao = self.entrada.get()
                # Cuidado: eval pode ser perigoso em aplicações reais!
                resultado = eval(expressao)
                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, str(resultado))
            except:
                messagebox.showerror("Erro", "Expressão inválida!")
        elif valor == 'C':
            self.entrada.delete(0, tk.END)
        elif valor == '√':
            self.entrada.insert(tk.END, 'math.sqrt(')
        elif valor in ['sin', 'cos', 'tan', 'log']:
            self.entrada.insert(tk.END, f'math.{valor}(')
        elif valor == 'π':
            self.entrada.insert(tk.END, str(math.pi))
        elif valor == '^':
            self.entrada.insert(tk.END, '**')
        else:
            self.entrada.insert(tk.END, valor)


# Execução
root = tk.Tk()
app = CalculadoraCientifica(root)
root.mainloop()

