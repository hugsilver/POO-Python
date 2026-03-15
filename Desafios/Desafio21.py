#Classe gamer com nome, nick e jogos favoritos
#Pode cadastar multiplos jogos
#Dois métodos: Cadastrar jogo e mostrar ficha
#Criar ficha com: Nick Name no titulo, nome real, jogos favoritos em ordem alfabetica

from rich import print
from rich.panel import Panel

#Criar classe
class gamer: #Método Construtor
    def __init__(self, name, nick):
        self.listagames = [] #Instânciando a lista
        self.name = name
        self.nick = nick
    
    def cadjogos(self, jogo): #Método cadastrar jogos
        
        self.listagames.append(jogo) #Recebendo o jogo na lista
        newlist = self.listagames.copy() #Copiando a lista em ordem alfabetica
        #print(newlist)
        self.newlist = newlist
    
    def ficha(self):
        nick = self.nick
        listord = sorted(self.newlist)
        games = "\n".join([f":video_game: - {game}" for game in listord])
        #Isso é uma list comprehension (forma curta de criar listas).
        #O f permite colocar variáveis dentro da string.
        #Agora vem a parte que junta tudo em um único texto. - "\n".join(lista)
        print(Panel(f'[white]Nome real:[/] [blue]{self.name}[/] [white]\nJogos favoritos:[/] \n[white]{games}[/]', title='Ficha do Jogador: '+nick, style='red', width=60))
        
#Programa principal
#Chamar os métodos

j1 = gamer('Juselino Cubicheca', 'JCC')
j1.cadjogos('Resident Evil')
j1.cadjogos('NFS')
j1.cadjogos('God Of War')
j1.ficha()

