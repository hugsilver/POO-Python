from rich import print


#Crie um classe Funcionario com nome, setor e cargo
#Crie um método que permita o funcionário se apresentar

#Return do método - Olá, sou {nome} e sou {cargo} dp setor de {setor} da empresa Curso em Vídeo 

#Bloco da classe
class Funcionario:

    def __init__(self, nome='Vazio', cargo='Vazio', setor='vazio', empresa='Curso em Vídeo'): #Método Construtor
        self.nome = nome
        self.cargo = cargo
        self.setor = setor
        #print(f'{self.nome}')

    def apresenta(self):    
        #return f'Olá, sou {self.nome}' #Return de um print formatado com as instancias
        print(f'Olá, sou [red]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa Curso em Video')
    
fu1 = Funcionario('Hugo', 'Programador', 'Automações')
fu1.apresenta()
print(fu1)






