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
t = 0
console = Console()

class Controle:
    def __init__(self):
        self.desliga_tv() #Começa desligado
        self.ch = 1
        self.volu = 1
        self.canais = [1, 2, 3, 4, 5]
    
    def liga_tv(self):#Método para ligar TV
        console.print(Panel(f"[white]CANAL: [/]{self.mostrar_canais()}\n\nVOLUME = {c1.mostrar_volume()}",title="[ TV ]",width=40))
        return 1
        
    def desliga_tv(self):#Método para desligar TV
        return print(Panel(':red_circle: [red] - A TV está desligada[/]', title='[ TV ] ', style='white', width=40)) #Faz o return do print tela desligada
    
    def canal(self, func=0):#Método para trocar de canal
        #Incremento e decremento
        if func == '>':
            self.ch += 1
        elif func == '<':
            self.ch -= 1
        #Limitadores
        if self.ch > 5:
            self.ch = 1 #Limita em 1 e reinciar caso passe de 5
        elif self.ch < 1:
            self.ch = 5
        #console.print(Panel(f"[white]CANAL: [/]{self.mostrar_canais()}\n\nVOLUME = {c1.mostrar_volume()}",title="[ TV ]",width=40))#Aqui mesmo - Deu certo
        return self.ch #Precisa retorna com o valor do canal atual
        
    def vol(self, func=0):#Método para aumentar ou diminuir volume
        #Incremento e decremento
        if func == '+':
            self.volu += 1
        elif func == '-':
            self.volu -= 1
        #Limitadores
        if self.volu > 4:
            self.volu = 4 #Limita em 4
        if self.volu < 1:
            self.volu = 1 #Limita em 1
        return self.volu #Precisa retorna com o valor do volume atual
    
    def mostrar_volume(self):#Método para representar a barra de colume
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
    
    def tratar_input(self):
        permitido = {'<', '>', '-', '+', '@', '0'}
        
        try:
            r = input(f'< CH >{c1.canal()} - VOL +{c1.vol()} ')
            
            if len(r) != 1 or r not in permitido:
                raise ValueError("Entrada inválida")
            
            return r

        except ValueError:
            self.desliga_tv()
            return None
            
c1 = Controle() #Instanciando objeto com a classe

while True:#Laço condicional infinito
    #r = input(f'< CH >{c1.canal()} - VOL +{c1.vol()} ')
    r = c1.tratar_input()  
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

#OBS.01:Não está modificando a tela (< , > , - , +), mas deveria aparecer que TV está desligada
#OBS.02: Ainda não está funcionando a renderização da tela quando TV ligada
