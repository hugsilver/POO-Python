from rich import print
from rich.panel import Panel

caixa = Panel('[white]Esse aqui é uma painel de exemplo[/]:+1:', title='Mensagem', style='red') #1° Texto e depois estilo
print(caixa)