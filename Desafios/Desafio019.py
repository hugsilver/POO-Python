
#Classe livro com quantidade de paginas = 100
#Usuario vai pode passar a pagina até o fim do livro

from rich import print
from rich.panel import Panel
from time import sleep

class livro: 
    def __init__(self, nome, pag=0): #Nome do livro e Quantidade de Páginas total
        self.capa = nome #Instânciando nome
        self.tp = pag #Instânciando total de páginas
        self.pgat = 1 #Instânciando página atual, iniciando com 1 sempre
        print(f'\nVocê acabou de abrir o livro [blue]{self.capa}[/] quem tem {self.tp} páginas no total. Agora você está na página 1')
    
    def passpg(self, num): #Método de passar página, recebendo o número de páginas para passar
        self.pgat += num #Acumulando a página atual, página atual recebe o acrescimo da qauntidade de páginas formadas
        if (self.pgat+num)>self.tp: #Condicional, se a soma da página atual mais o incremento for maior que o total de páginas, entra nessa condição
            self.sim(self.pgat-num, self.tp+1) #Chama a função, passando pg inicial (Atual) e final(Total)
            print(f'\nO livro [blue]{self.capa}[/] tem {self.tp} paginás, você avançou até o final das {self.tp}, [red]NÃO TEM COMO AVANÇAR MAIS QUE ISSO!!![/]')
        else:#Caso contrario, a função entra nessa condição
            self.sim(self.pgat- num, self.pgat) #Recebe a quantidade de páginas que é para passar e o atributo final (Pg atual)
            print(f'\nVocê passou {num} páginas, sua página atual é {self.pgat}')

    def sim(self, inicio, fim): #Função para criar 'animação'
        for c in range(inicio, fim): #Recebe inicio (Página atual) e fim(Página atual + num)
            print('Pg.',c , '->', end=' ')
            sleep(0.5)
            
pg = livro('Meu mundo invertido', 20)
pg.passpg(5)
pg.passpg(6)
pg.passpg(10)


    





