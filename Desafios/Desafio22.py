#Criar classe Controle remoto
#Com métodos de funcionamento: Canal (<(Voltar 1 canal) e >(Avançar 1 canal)), volume (+ e -), liga e desliga (Somente um pelo @)
#@ para Ligar ou Desligar, 0 - sai do programa
#OBS: Já inicia com canal desligado, inicial no canal 1 (Podendo avnaçar até o 5 e se avançar mais retorna para o 1), volume inicial na graduação baixa 20%
#Volume chegando no máximo, não avança mais, tbm deve ter limite de mínimo - tbm se mantem
# #Usar marcação dos canais e barra de progresso para o volume 

from rich import print
from rich.panel import Panel
count = 0

class Controle:
    def __init__(self, status=False):
        self.desliga_tv()
        self.ch = 1
        self.volu = 1
    
    def liga_tv(self):
        print(Panel(':green_circle: [green] - A TV está ligada[/]', title='[ TV ] ', style='white', width=40))
        self.sts = 1
        return self.sts
        
    def desliga_tv(self):
        print(Panel(':red_circle: [red] - A TV está desligada[/]', title='[ TV ] ', style='white', width=40))
        self.sts = 0
        return self.sts
    
    def canal(self, func=0):#1° Criar o layout com troca de canal
        if func == '>':
            self.ch += 1
        elif func == '<':
            self.ch -= 1
        #Limitadores
        if self.ch > 5: # or self.ch < 1
            self.ch = 1 #Limita em 1 e reinciar caso passe de 5
        elif self.ch < 1:
            self.ch = 5
        return self.ch
    
    def vol(self, func=0):#3° Criar o layout com a barra de progresso e colocar o limitador
        if func == '+':
            self.volu += 1
        elif func == '-':
            self.volu -= 1
        #Limitadores
        if self.volu > 4:
            self.volu = 4 #Limita em 4
        if self.volu < 1:
            self.volu = 1 #Limita em 1
        return self.volu
        
c1 = Controle()

while True:
    r = input(f'< CH >{c1.canal()} - VOL +{c1.vol()} ')  
    
    if r == '@':
        count += 1
        if count%2 != 0:
            c1.liga_tv()
        else:
            c1.desliga_tv()
    if c1.liga_tv == 1:
        if r == '<' or '>':
            c1.canal(r)
        if r == '+' or '-': 
            c1.vol(r)
    if r == '0':
        break

#OBS: 1° TV mesmo desligada está recebendo os comandos AJUSTAR