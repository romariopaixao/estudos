import tkinter as tk
from tkinter import messagebox

def exibir_mensagem():
    nome = entrada_nome.get()
    if nome:
        mensagem = f"Bem-vindo, {nome}!"
        messagebox.showinfo("Mensagem de Boas-vindas", mensagem)
    else:
        messagebox.showwarning("Aviso", "Por favor, digite seu nome.")

# Criar a janela principal
janela = tk.Tk()
janela.title("Sistema de Cadastro")

# Criar o campo de entrada
entrada_nome = tk.Entry(janela, width=30)
entrada_nome.pack(pady=10)

# Criar o botão
botao_enviar = tk.Button(janela, text="Enviar", command=exibir_mensagem)
botao_enviar.pack()

# Iniciar o loop da janela
janela.mainloop()