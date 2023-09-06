def center(win):  #Essa função eu peguei da internet para centralizar a interface
    win.update_idletasks()  
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

from tkinter import * #Importação da biblioteca tkinter para fazer as janela

def enviar(): #Função do botão para mostrar a mensagem completa
    nome = caixa1.get()
    mensagem = caixa2.get() 
    msg["text"] = nome, "diz:", mensagem 

def fechar_pag(): #Função para fechar a primera página quando clicar no botão
    janela.destroy()

def maiusc_1(): #Função para a primeira letra ser maiúscula
    texto_entrada = caixa1.get()
    texto_formatado = texto_entrada.capitalize()
    caixa1.delete (0, END)
    caixa1.insert (0, texto_formatado)

def maiusc_2(): #Função para a primeira letra ser maiúscula
    texto_entrada = caixa2.get()
    texto_formatado = texto_entrada.capitalize()
    caixa2.delete (0, END)
    caixa2.insert (0, texto_formatado)

def prox(event): #Função para passar para a próxima caixa de texto
    caixa2.focus_set() 

janela = Tk() #Criação da primeira janela e abaixo suas especificações
janela.geometry("400x200")
janela.config(bg="#ADD8E6")
janela.title("Avaliação Diagnóstica")

titulo = Label (janela, text="Sou o Arthur Gonçalves e sei fazer ;p - 2° Semestre - UNIVALE",fg="#2F4F4F", font="Arial 10 bold", bg="#ADD8E6") #Aqui é dado o título da página
titulo.grid (column=2, row=0)

subtitulo = Label (janela, text="Nome:", bg="#ADD8E6") #Adiciona o texto "nome"
subtitulo.place(x=0, y=20)

caixa1 = Entry(janela, background="gray", width=30, font="Arial 10") #Inserção do nome
caixa1.place(x=10, y=40)
caixa1.bind("<KeyRelease>", lambda event= None: maiusc_1())

subtitulo2 = Label (janela, text="Mensagem:",bg="#ADD8E6") #Adiciona o texto "mensagem"
subtitulo2.place(x=0,y=60)

caixa2 = Entry(janela, background="gray", width=30, font="Arial 10") #inserção da mensagem
caixa2.place(x=10, y=80)
caixa2.bind("<KeyRelease>", lambda event= None: maiusc_2())
caixa1.bind("<Return>",prox)
caixa1.focus_set()

botao = Button(janela, text="Enviar", command=lambda: [enviar(), fechar_pag()] ,width=55) #Criação do botão enviar com dois comandos, o de enviar a mensagem e fechar a página
botao.place(x=2,y=110)

janela2 = Tk() #Criação da segunda página 
janela2.title("Segundo Semestre")
janela2.geometry("500x350")
janela2.config(bg="#ADD8E6")

msg = Label(janela2, text="Aguardando mensagem...", bg="#ADD8E6", font="Arial 15 bold", fg="#2F4F4F") #Aqui irá mostrar a mensagem com nome
msg.place(x=80,y=80)

center(janela2) #Função para centralizar a página 2
center(janela) #Função para centralizar a página 1

janela = mainloop() #Aqui ele irá permitir que a página fique aberta até ser fechada pelo usuário
