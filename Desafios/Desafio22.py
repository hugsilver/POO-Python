#Criar classe Controle remoto
#Com métodos de funcionamento: Canal (<(Voltar 1 canal) e >(Avançar 1 canal)), volume (+ e -), liga e desliga (Somente um pelo @)
#@ para Ligar ou Desligar, 0 - sai do programa
#OBS: Já inicia com canal desligado, inicial no canal 1 (Podendo avnaçar até o 5 e se avançar mais retorna para o 1), volume inicial na graduação baixa 20%
#Volume chegando no máximo, não avança mais, tbm deve ter limite de mínimo - tbm se mantem
# #Usar marcação dos canais e barra de progresso para o volume 

from rich import print
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn
from rich.console import Console

count = 0
console = Console()

class Controle:
    def __init__(self, status=False):
        self.desliga_tv() #Começa desligado
        self.ch = 1
        self.volu = 1
        self.canais = [1, 2, 3, 4, 5]
    
    def liga_tv(self):
        console.print(Panel(f"[white]CANAL: [/]{self.mostrar_canais()}\n\nVOLUME = {c1.mostrar_volume()}",title="[ TV ]",width=40))
        return 1
        
    def desliga_tv(self):
        print(Panel(':red_circle: [red] - A TV está desligada[/]', title='[ TV ] ', style='white', width=40))
    
    def canal(self, func=0):#1Método para trocar de canaç
        if func == '>':
            self.ch += 1
        elif func == '<':
            self.ch -= 1
        #Limitadores
        if self.ch > 5:
            self.ch = 1 #Limita em 1 e reinciar caso passe de 5
        elif self.ch < 1:
            self.ch = 5
        console.print(Panel(f"[white]CANAL: [/]{self.mostrar_canais()}\n\nVOLUME = {c1.mostrar_volume()}",title="[ TV ]",width=40))#Aqui mesmo - Deu certo
        return self.ch
        
    def vol(self, func=0):#Método para aumentar ou diminuir volume
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
    
    def mostrar_volume(self):#Método para representar a barra de columw
        barra = "█" * self.volu + "░" * (4 - self.volu)
        return f"[green]{barra}[/]"
    
    def mostrar_canais(self):#Método para representar o canal selecionado
        texto = ""
        for c in self.canais:
            if c == self.ch:
                texto += f"[black on yellow] {c} [/] "
            else:
                texto += f"[white]{c}[/] "
        return texto
            
c1 = Controle() #Instanciando objeto com a classe

while True:#Laçõ condicional infinito
    #print(f'1° CONTADOR: {count}')#Contadores estão funcionando
    r = input(f'< CH >{c1.canal()} - VOL +{c1.vol()} ')  
    if r == '@':
        count += 1
        if count%2 != 0:
            #print(f'2° CONTADOR: {count}')
            t = c1.liga_tv()#Chama método de ligar TV
        else:
            #print(f'3° CONTADOR: {count}')
            c1.desliga_tv()
    if t == 1: #Métodos de volume só ativo se TV Ligada, sé entrar na condição de TV ligada
        if r == '<' or '>':
            c1.canal(r)
        if r == '+' or '-': 
            c1.vol(r)
    if r == '0':
        break

#OBS.01:Está dando erro com 0 ou com qualquer outro comando (< , > , - , +) quando desligada - Ajustar
