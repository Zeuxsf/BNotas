#Imports
import customtkinter as ctk
import tkinter
import os

#Configurações da janela principal
janela = ctk.CTk(fg_color='snow2')
janela.title('B-Notas')
janela.geometry('720x600')
janela.resizable(False,False)

#Textos da janela principal
#Título:
ctk.CTkLabel(janela,text='B-NOTAS',text_color='systemhighlight',font=('Arial Black',40)).place(y=10,x=270)
#Nome da nota:
ctk.CTkLabel(janela,text='Nome da Nota:', text_color='systemhighlight',font=('Arial Black',20)).place(y=120,x=35)
#Bloco de Notas:
ctk.CTkLabel(janela,text='Sua Nota:',text_color='systemhighlight',font=('Arial Black',20)).place(y=160,x=35)

#Entrada do nome da nota:
nome = ctk.CTkEntry(janela,placeholder_text='Nome...',fg_color='snow2',text_color='black',border_color='systemhighlight')
nome.place(y=120,x=200)

#O Bloco de notas em si:
nota = ctk.CTkTextbox(janela,fg_color='snow',width=400,height=400,text_color='black',scrollbar_button_color='systemhighlight',scrollbar_button_hover_color='SkyBlue')
nota.place(y=160,x=150)

#Função de salvar a nota:
def save():
    nomesalvo = nome.get()
    notasalva = nota.get('1.0','end')

    #Vai Salvar a nota dentro de um arquivo com o nome dentro de 'nomesalvo'
    with open(nomesalvo,'w') as arquivo:
        arquivo.write(notasalva)
    
    #Vai criar um arquivo 'NotasSalvas' caso esse arquivo não exista, para não dar erro
    if not os.path.exists('NotasSalvas.txt'):
        open('NotasSalvas.txt', 'a').close()

    #Vai verificar se a nota ja existe, assim o programa só vai modificar ela
    with open('NotasSalvas.txt','r') as verif:
        notas = verif.readlines()

    #Se a nota não existir, vai criar uma nova
    if nomesalvo + '\n'  not in notas:    
        with open('NotasSalvas.txt', 'a') as arquivo000:
            arquivo000.write(nomesalvo + '\n')  

    print('Nota Salva!')    
    pass

#Função para verificar quais notas estão salvas:
def salvas():
    #Vai criar um arquivo 'NotasSalvas' caso esse arquivo não exista, para não dar erro
    if not os.path.exists('NotasSalvas.txt'):
        open('NotasSalvas.txt', 'a').close()
    
    #Configurações da nova janela, janela que só vai servir para carregar notas salvas
    saved = ctk.CTkToplevel(janela,fg_color='snow2')
    saved.geometry('380x380')
    saved.resizable(False,False)
    saved.title('Notas Salvas')

    #Um texto box para mostrar as notas salvas
    savednotes = ctk.CTkTextbox(saved,400,345,font=('Arial Black',20),border_color='systemhighlight',border_width=1,bg_color='systemhighlight',text_color='black',fg_color='snow',scrollbar_button_color='systemhighlight',scrollbar_button_hover_color='SkyBlue')
    savednotes.pack()

    #Função que vai carregar as notas no Bloco principal
    def load():
        nomecarregado = savedname.get()

        #Vai ler a nota chamada
        with open(nomecarregado,'r') as arquivo:
            conteudo = arquivo.read()

            #Vai deletar o conteúdo da nota principal
            nota.delete('1.0', 'end')
            #Vai adicionar a nota carregada na nota principal
            nota.insert('1.0', conteudo)

            #Vai deletar o Nome no bloco principal
            nome.delete(0,'end')
            #Vai adicionar o Nome da nota carregada no bloco principal
            nome.insert(0,nomecarregado)
            print('Nota Carregada!')

            #Depois de carregar uma nota, a janela vai ser fechada
            saved.destroy()

    #Um subtítulo da janela
    ctk.CTkLabel(saved,text='NOTAS:',font=('Arial Black', 20),text_color='systemhighlight').place(y=348,x=3)
    
    #Vai receber o nome da nota a ser carregada
    savedname = ctk.CTkEntry(saved,text_color='black',fg_color='snow',placeholder_text='Escreva o Nome da Nota',border_color='systemhighlight',width=170)
    savedname.place(y=348,x=95)

    #Botão: Carregar nota no bloco principal
    ctk.CTkButton(saved,text='Carregar',fg_color='systemhighlight',hover_color='SkyBlue',width=100,command=load).place(y=348,x=270)

    #Vai mostrar as notas salvas em um textbox e não vai permitir o usuário alterá-lo
    with open('NotasSalvas.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        savednotes.insert('1.0',conteudo)
        savednotes.configure(state='disabled')

#Função para apagar notas
def apaga():
    name = nome.get()

    #Vai criar um arquivo 'NotasSalvas' caso esse arquivo não exista, para não dar erro
    if not os.path.exists('NotasSalvas.txt'):
        open('NotasSalvas.txt', 'a').close()

    #Vai ler quai notas estão salvas
    with open('NotasSalvas.txt','r') as arquivo:
        linhas = arquivo.readlines()

    #Vai excluir a nota chamada
    with open('NotasSalvas.txt', 'w') as arquivo:
        for linha in linhas:
            if linha.strip() != name:
                arquivo.write(linha)

    #Vai verificar se existe um arquivo com o nome dentro de 'name'
    #se sim: vai excluir o arquivo
    if os.path.exists(name):
        os.remove(name)            


#Botão: Salvar
salvar = ctk.CTkButton(janela,text='Salvar',fg_color='springgreen4',hover_color='green3',command=save)
salvar.place(y=180,x=565)

#Botão: Notas salvas
carregar = ctk.CTkButton(janela, text='Notas Salvas',fg_color='systemhighlight',hover_color='SkyBlue',command=salvas)
carregar.place(y=235,x=565)

#Botão: Apagar 
apagar = ctk.CTkButton(janela, text='Apagar Nota',fg_color='red4',hover_color='orangered4',command=apaga)
apagar.place(y=290,x=565)

#Mantém a janela principal aberta
janela.mainloop()
