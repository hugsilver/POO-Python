#Classe caneta - Frase na cor relativa e texto
#Métodos Destampar e escrever

from rich import print

class Caneta:
    def __init__(self, cor):#Bloco construtor
        if cor == 'azul':
            self.cor = 'blue'
        elif cor == 'vermelho':
            self.cor = 'red'
        elif cor == 'verde':
            self.cor = 'green'

        
        self.resp = False #Caneta Inicia Tampada
    
    def destampar(self):#Método para destampar caneta
        self.resp = True
    
    def escrever(self, text=0):#Método para escrever o texto
        self.text = text
        if self.resp == True:
            print(f'[{self.cor}]{self.text}[/]')
        elif self.resp ==  False:
            print('A [blue]caneta[/] está tampada!!!')
    
    def quebrar_linha(self, n=1):
        print('\n'*n)

c1 = Caneta('azul')
c1.destampar()
c1.escrever('Olá, tudo bem? ')
#c1.quebrar_linha(1)

c2 = Caneta('verde')
c2.destampar()
c2.escrever('Vamos que vamos')
#c2.quebrar_linha(2)

c3 = Caneta('vermelho')
c3.destampar()
c3.escrever('Será que foi?')
#c3.quebrar_linha()

