#Declaração de Classe - Não gera nada, é somente definição
class Gafanhoto:
    '''
Essa classe cria um gafanhoto, que tem nome e idade;
Para criar uma nova pessao, use
variavel = Gafanhoto(nome, idade)
    
    '''
    def __init__(self, nome = 'Vazio', idade = 0): #Método Construtor
        #nome e idade opcional
        #Átributos de Instância
        self.nome = nome #Parametro que chegou da função
        self.idade = idade #Parametro que chegou da função
        #self.idade - Atributo da instância
        #Criou o molde, não criou objeto
        #Self - Busca ele mesmo
        #OBS: O ideal não é mexer direto nos atributos, pois quera o encapsulamento 
        #Mas sim fazer por métodos
        #Self é obrigátorio por ser um método
    
    #Método de Instância
    def aniversario(self):
        self.idade = self.idade + 1 #Mexe no atributo de idade
        #sefl.idade += 1
    
    def __str__(self): #Dunder Method
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."
    
    def __getstate__(self):
        return f'Estado: nome = {self.nome} ;  idade = {self.idade}'


#Declaração de Objetos
#Para  ter um objeto, tem que instânciar esse objeto com uma classe

g1 = Gafanhoto('Maria', 17) #Inicializou com 17
g1.aniversario() #Método - () é um método ; Chamou a classe para adicionar aniversario
#OBS:
#Se tiver nada no fim, é um atributo
#Se tiver () é um método

#g1 - Objeto
#() - Chama o método construtor

#print(g1)
#print(g1.__doc__) #Dunder Attribute - Sempre documentar sua classe
print(g1.__dict__) #Mostar exibição de forma de dicionario - Atributo
print(g1.__getstate__()) #Método - Que pode ser personalizavel
print(g1.__class__) #Mais um Dunder Attribute 

#Ficar ligado em
#1° Inicializar utilizando parametros
#2° Dunder attritutes: Doc, Class, Dict
#3° Dunder Methods: State e srt






