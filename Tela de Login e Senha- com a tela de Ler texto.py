#=========================
#As Bibliotecas do Sistema
#=========================
from tkinter import ttk
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb

#=================
# Codigos do Programa
#=================
class PrincipalRAD:
    def __init__(self,win):
        self.login = tk.Label(win, text='Login')#Texto do Login
        self.login.place(x=0, y=0)
        
        self.texto = tk.Entry(bd=3, bg='#e3e344')#Onde vai digitar O Login
        self.texto.place(x=40, y=0)
        
        self.Senha = tk.Label(win, text='Senha')#Texto da Senha
        self.Senha.place(x=0, y=40)
        
        self.texto2 = tk.Entry(bd=3, bg='#e3e344')#Onde vai digitar A Senha
        self.texto2.place(x=40, y=40)
        
        #Botão onde ira Carregar Login e Senha
        style = ttk.Style()
        self.btn = ttk.Button(win, text='Entrar', command=self.teste)
        style.theme_use('alt')
        style.configure('TButton', font=('American typewriter', 14), background='#232323', foreground='white')
        style.map('TButton', background=[('active', '#ff0000')])
        self.btn.place(x=40, y=80)
        
    def teste(self):
        login = self.texto.get()#Pega o dados do Login
        senha = self.texto2.get()#Pega o dados da Senha
        if login == 'ihury' and senha == '123':#onde vai Confirmar se o login e Senha, confere com os dados a Cima
            print('Login e Senha Confirmada')
            janela2 = Toplevel()#criamos a janela
            E = Text(janela2)#criamos o widget Text.
            x=open("aula.txt","r") #função de abertura para ler
            z = x.read() #função ler, read
            E.insert(0.0,z)#aqui inserimos o texto dentro do widget Text.
            E.pack()#empacotanos o widget Text
            janela2.mainloop()#fazemos o loop da janela.
        else:
            mb.showerror('Erro', 'Dados incorretos, Tenta novamente!!')
            print('Dados de usuario incorretos')# Sé acaso o usuario digitar algo errado

#=======================
# Janela Principal do programa, onde ira aparecer as informação!
#=======================            
janela = tk.Tk()
view = PrincipalRAD(janela)
janela.title('Sistema de Ragnarok (Beta)')
janela.geometry('200x120+0+0')
janela.mainloop()