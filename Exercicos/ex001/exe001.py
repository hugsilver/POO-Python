#Declaração de Classe - Não gera nada, é somente definição
class Gafanhoto:
    def __init__(self): #Método Construtor
        #Átributos de Instância
        self.nome = ''
        self.idade = 0
        #Criou o molde, não criou objeto
        #Self - Busca ele mesmo
        #OBS: O ideal não é mexer direto nos atributos, pois quera o encapsulamento 
    
    #Método de Instância
    def aniversario(self):
        self.idade = self.idade + 1 #Mexe no atributo de idade
        #sefl.idade += 1
    
    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."


#Declaração de Objetos
#Para  ter um objeto, tem que instânciar esse objeto com uma classe

g1 = Gafanhoto()
g1.nome = 'Maria' #Atributo nome
g1.idade = 17 #Atributo idade
g1.aniversario() #Método - () é um método
#OBS:
#Se tiver nada no fim, é um atributo
#Se tiver () é um método

#g1 - Objeto
#() - Chama o método construtor

print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = 'Mauro'
g2.idade = 53
g2.aniversario()

print(g2.mensagem())

#Obs: As linhas de declaração de classe não precisam estar no mesmo código que a declaração de obejto

g3 = Gafanhoto()
print(g3.mensagem())




