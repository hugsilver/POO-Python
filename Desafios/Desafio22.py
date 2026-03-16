#Criar classe Controle remoto
#Com métodos de funcionamento: Canal (<(Voltar 1 canal) e >(Avançar 1 canal)), volume (+ e -), liga e desliga (Somente um pelo @)
#@ para Ligar ou Desligar, 0 - sai do programa
#OBS: Já inicia com canal desligado, inicial no canal 1 (Podendo avnaçar até o 5 e se avançar mais retorna para o 1), volume inicial na graduação baixa 20%
#Volume chegando no máximo, não avança mais, tbm deve ter limite de mínimo - tbm se mantem
# #Usar marcação dos canais e barra de progresso para o volume 

#Iniciar pela construção da tela

from rich import print
from rich.panel import Panel

class Controle:
    def __init__(self, status=False):
        if status == False:
             print(Panel(':red_circle: [red] - A TV está desligada[/]', title='[ TV ] ', style='white', width=40))

        elif status == '@':
            print('Ligou')
    
    def canal(self, func=0):
        if func == '>':
            ch += 1
        elif func == '<':
            ch -= 1
        return ch

c1 = Controle()

while True:    
    s = input(f'< CH{canal()} > ')

    if s =='<' or s =='>':
        c1.canal('s')
    
    if s == '0':
        break

