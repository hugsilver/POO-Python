#Crie uma classe Produto com nome e preço
#Crie um método que crie uma etiqueta de produto

from rich import print
from rich.panel import Panel

def linha(tl):
    return '-'*tl

class Produto:

    def __init__(self, nome_prod='vazio', preço=0): #Método Construtor
        self.nome_prod = nome_prod
        self.preço = preço
        #print(f'{self.nome_prod}')

    def etiqueta(self):
        
        #Caixa = Panel('[white]{self.nome}}[/]', title='Produto', style='red')
        l1 = linha(26)
        var = str(self.preço)
        l2 = linha(len(var)+4)
        #print(l2) 
        #print(Panel(f'[white]{self.nome_prod.center(32 - len(self.nome_prod))}\n{self.preço:,.2f}[/]', title='Produto', style='red', width=30)) # Teste 3
        #print(Panel(f'[white]{linha()}[/]'.center(28+len(self.nome_prod)))) # Teste 2
        print(Panel(f'[white]{self.nome_prod.center(32 - len(self.nome_prod))}[/]\n[white]{l1}\n{l2}R${self.preço:,.2f}{l2}[/]', title='Produto', style='red', width=30))
        #Acredito que possa ser otimizado - Talvez criar uma função para ler o tamanho e retorna somente o tamanho certo para o center
        #print(len(var))
           

prod1 = Produto('MacBook', 6_000)
prod2 = Produto('Iphone 17', 8_900)
prod1.etiqueta()
prod2.etiqueta()

    






