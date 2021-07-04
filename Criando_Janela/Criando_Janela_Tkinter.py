from tkinter import * #Biblioteca que to usando para Criar a Janela
# E a Estrela(*) e para puxar tudo que tem na biblioteca Tkinter
from PIL import ImageTk as img

janela = Tk()# Janela
janela.title('Mostrando a janela') #Titulo da janela
janela.geometry('800x600')# Altura e largura da janela
janela.configure(bg='grey')# A cor do fundo da janela
janela.iconbitmap('Artc.ico')# Adicionando Icone para Janela

imagem_ = img.PhotoImage(file="Artc.ico")# pegando o arquivo da imagem
Label(janela, image=imagem_ ,bg='#292826',pady=0).pack(padx=5, pady=180)#adicionando a imagem no fundo da jenale

janela.mainloop() # Abrindo a janela