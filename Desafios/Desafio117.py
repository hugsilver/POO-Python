#Crie uma classe Produto com nome e preço
#Crie um método que crie uma etiqueta de produto

from rich import print
from rich.panel import Panel

def linha():
    return print('-'*28)

class Produto:

    def __init__(self, nome_prod='vazio', preço=0): #Método Construtor
        self.nome_prod = nome_prod
        self.preço = preço
        #print(f'{self.nome_prod}')

    def etiqueta(self):
        
        #Caixa = Panel('[white]{self.nome}}[/]', title='Produto', style='red')
        #l = linha()
        print(Panel(f'[white]{self.nome_prod}[/]', title='Produto', style='red', width=30))

    
prod1 = Produto('MacBook', 6_000)
prod1.etiqueta()
#print(prod1)
    






