#Classe churrasco com quantidade de pessoas que irão participar 
#Return quantidade de carne, custo toal, preço por pessoa.
#Considere:
#Consumo padrão: 400g por pessoa
#Preço: R$82,40/kg

from rich import print
from rich.panel import Panel

class Churrasco:
    def __init__(self, titulo, quant):
        self.nome =  titulo
        self.participantes = quant
    
    def analisar(self):
        ti = self.nome
        tot_carn = self.participantes*0.4
        tot = tot_carn*82.40
        var_ppartipante = tot/self.participantes
        print(Panel(f'Analisando [green]{self.nome}[/] com [blue]{self.participantes} convidados[/]\n[white]Cada participante comera 0.4Kg e cada Kg custa R$82.40[/]\nRecomendo [blue]comprar {tot_carn}Kg[/] de carne\nO custo total será de [green]R${tot:,.2f}[/]\nCada pessoas pagara [yellow]R${var_ppartipante}[/] para participar.', title=ti, style='white', width=90))
        #print(Panel(f'[white]{self.nome_prod.center(32 - len(self.nome_prod))}[/]\n[white]{l1}\n{l2}R${self.preço:,.2f}{l2}[/]', title='Produto', style='red', width=30))


c1 = Churrasco('Churrasco dos Amigos', 2000)
c1.analisar()













