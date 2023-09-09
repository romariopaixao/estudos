from tkinter import *
from tkinter import messagebox
from tkinter import ttk

agenda = []
index = None


#funcoes
def adicionarContato() -> None:
    nome = txt_nome.get()
    telefone = txt_telefone.get()
    categoria =cb_categorias.get()
    contato = {
        'nome': nome,
        'telefone': telefone,
        'categoria': categoria
    }
    agenda.append(contato)
    messagebox.showinfo('Adicionado!', 'Contato adicionado com sucesso!')
    limparCampos()
    atualizarTabela()

def atualizarTabela() -> None:
    #limpando a tabela
    #get_children -> retorna uma lista com todas as linhas da tabela
    for linha in tabela.get_children():
        tabela.delete(linha)

    for contato in agenda:
        tabela.insert('', END, values=(contato['nome'], contato['telefone'], contato['categoria']))

def editarContato() -> None:
    agenda[index] = {
        'nome': txt_nome.get(),
        'telefone': txt_telefone.get(),
        'categoria': cb_categorias.get()
    }
    limparCampos()
    atualizarTabela()
    messagebox.showinfo('Alterado', 'Dados alterados com sucesso!')

def deletarContato() -> None:
    agenda.remove(agenda[index])
    limparCampos()
    atualizarTabela()
    messagebox.showinfo('Deletando!', 'Contato removido com sucesso!')

def limparCampos() -> None:
    txt_nome.delete(0, END)
    txt_telefone.delete(0, END)
    cb_categorias.delete(0, END)

def tabelaClique(event) -> None:
    #Para pegar no console se a bind ta funcionando -> print(type(event))
    contato_selecionado = tabela.selection()[0]
    if not contato_selecionado:
        return
    global index
    # Pegando o indice da linha da coluna
    index = tabela.index(contato_selecionado)
    contato = agenda[index]
    limparCampos()
    txt_nome.insert(0, contato['nome'])
    txt_telefone.insert(0, contato['telefone'])
    cb_categorias.set(contato['categoria'])

janela = Tk()
#Adicionar título a janela
janela.title('Agenda Telefonica')

# Label
label_nome = Label(janela, text='Nome', fg='navy', font='Tahoma 14 bold')
label_nome.grid(row=0, column=0)

label_telefone = Label(janela, text='Telefone', fg='navy', font='Tahoma 14 bold')
label_telefone.grid(row=1, column=0)

label_categoria = Label(janela, text='Categoria', fg='navy', font='Tahoma 14 bold')
label_categoria.grid(row=2, column=0)

# Como criar um comboBox
categorias = ['Amigos', 'Familia', 'Trabalho']
cb_categorias = ttk.Combobox(janela, values=categorias, width=25, font='Tahoma 14')
cb_categorias.grid(row=2, column=1)

# Entry
txt_nome = Entry(janela, font='Tahoma 14', width=27)
txt_nome.grid(row=0, column=1)
txt_telefone = Entry(janela, font='Tahoma 14', width=27)
txt_telefone.grid(row=1, column=1)

# Botões
btn_adicionar = Button(janela, text='Adicionar', fg='navy', bg='white', font='Tahoma 12 bold', width=8, height=1, command=adicionarContato)
btn_adicionar.grid(row=3, column=0)

btn_editar = Button(janela, text='Editar', fg='navy', bg='white', font='Tahoma 12 bold', width=8, height=1, command=editarContato)
btn_editar.grid(row=3, column=1)

btn_deletar = Button(janela, text='Deletar', fg='navy', bg='white', font='Tahoma 12 bold', width=8, height=1, command=deletarContato)
btn_deletar.grid(row=3, column=2)

#tabela
#columns: Colunas do cabeçalho
#show=headings: para exibir o cabeçalho da tabela
tabela = ttk.Treeview(janela, columns=('Nome', 'Telefone', 'Categoria'), show='headings')
tabela.heading('Nome', text='Nome')
tabela.heading('Categoria', text='Categoria')
tabela.heading('Telefone', text='Telefone')
tabela.grid(row=4, columnspan=3)
# Como criar um evento/ação
tabela.bind('<ButtonRelease-1>', tabelaClique)


#loop para manter a janela aberta
janela.mainloop()