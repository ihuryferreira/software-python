#Criando Sistema da Maneira Correta
#Bem Basico

import tkinter as tk

class PricipalRAD:
	def __init__(self,win):

		self.texto = tk.Label(win, text='Olá Mundo!')
		self.texto.pack()

		self.separador = tk.Label(win, text='='*15)
		self.separador.pack()

		self.windo = None

		self.widget1 = tk.Frame(self.windo)
		self.widget1.pack()

		self.texto2 = tk.Label(self.widget1, text='Criando Conta de Mais', fg='blue')
		self.texto2['font'] = ('Verdana', '10', 'italic', 'bold')
		self.texto2.pack()

		self.separador2 = tk.Label(win, text='='*15)
		self.separador2.pack()

		self.num = tk.Label(win, text='Digite O primeiro número:')
		self.num.pack()

		self.numDados = tk.Entry(win, bd=3)
		self.numDados.pack()

		self.num2 = tk.Label(win, text='Digite O Segundo número: ')
		self.num2.pack()

		self.num2Dados = tk.Entry(win, bd=3)
		self.num2Dados.pack()

		self.botao = tk.Button(win, text='Clique Aqui para Fazer a Soma', bg='blue', fg='white', command=self.Soma)
		self.botao['font'] = ('Verdana', '15', 'italic', 'bold')
		self.botao.pack()

		self.resutado = tk.Label(win, text='', fg='red')
		self.resutado.pack()

	def Soma(self):
		n = int(self.numDados.get())
		n2 = int(self.num2Dados.get())

		soma = n + n2

		self.resutado['text'] = soma

janela = tk.Tk()
janela.title('Criando Sistema Basico com Python')
view = PricipalRAD(janela)
janela.mainloop()