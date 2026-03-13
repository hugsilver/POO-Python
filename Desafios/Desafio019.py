
#Classe livro com quantidade de paginas = 100
#Usuario vai pode passar a pagina até o fim do livro

from rich import print
from rich.panel import Panel

class livro:
    def __init__(self, nome, pag=0):
        self.capa = nome
        self.tp = pag
        self.pgat = 1
        print(f'\nVocê acabou de abrir o livro [blue]{self.capa}[/] quem tem {self.tp} páginas no total. Agora você está na página 1')
    
    def passpg(self, num):
        self.pgat += num
        if (self.pgat+num)>self.tp:
            self.sim(self.tp - self.pgat)
            print(f'\nO livro [blue]{self.capa}[/] tem {self.tp} paginás, você avançou até o final das {self.tp}, [red]NÃO TEM COMO AVANÇAR MAIS QUE ISSO!!![/]')
        else:
            self.sim(num)
            print(f'\nVocê passou {num} páginas, sua página atual é {self.pgat}')

    def sim(self, num):
        for c in range(self.pgat-num, self.pgat+1):
            print('Pg.',c , '->', end=' ')
            
pg = livro('Meu mundo invertido', 20)
pg.passpg(5)
pg.passpg(6)
pg.passpg(10)


    





