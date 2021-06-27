from tkinter import*

janela = Tk()#criamos a janela

janela.title('janela com abertura de texto')

E = Text(janela)#criamos o widget Text.

x=open("aula.txt","r") #função de abertura para ler

z = x.read() #função ler, read

E.insert(0.0,z)#aqui inserimos o texto dentro do widget Text.

E.pack()#empacotanos o widget Text

#btn = Button(text='Confirmar', command=dado) #Botão para confirmar o texto Salvo // mais fechei para deixar apenas o texto
#btn.pack()

janela.mainloop()#fazemos o loop da janela.