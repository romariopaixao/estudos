from tkinter import *

janela = Tk()
janela.title('Label')
janela.geometry('500x500')

contador = 0
def executar():
    global contador
    texto_1 = 'Numero par: '
    texto_2 = 'Numero impar: '
    if contador % 2 == 0:
        resultado = texto_1 + str(contador)
        #muda a cor e texto do label_pais
        label_pais['text'] = resultado
        label_pais['fg'] = '#24851e'
    else:
        resultado = texto_2 + str(contador)
        # muda a cor e texto do label_pais
        label_pais['text'] = resultado
        label_pais['fg'] = '#2586c2'
    contador += 1



#criando label com tamanho largura, nome, font e tamanho da font, cor da letra e fundo
label_nome = Label(janela, width=10, height=2, text='Nome: ', font=('Arial 15'), fg='#fc3503', bg='black')
label_nome.grid(row=0, column=0, padx=5, pady=10)


#criando label com tamanho largura, nome, font e tamanho da font, cor da letra e fundo
label_idade = Label(janela, width=10, height=2, text='Idade: ', font=('Arial 15'), fg='#429639', bg='black')
label_idade.grid(row=0, column=1, pady=10)

#criando label com tamanho largura, nome, font e tamanho da font, cor da letra e fundo
label_pais = Label(janela, width=15, height=2, text='Pais: ', font=('Arial 15'), fg='#6168e8', bg='black')
label_pais.grid(row=2, column=0, pady=10)

button = Button(janela, command=executar, width=8, height=1, text='Clique aqui', relief='raised', fg='black', bg='white')
button.grid(row=2, column=1, padx=10)

janela.mainloop()