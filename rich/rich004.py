from rich import print
from rich import inspect

#print(int.__dict__)
inspect(int, all=True)


class ContaBancaria: #Criação da classe
    '''
    Cria uma conta bancaria e permite fazer saques e depositos
    '''
    #Trabalhar no método construtor
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta {self.id} criada com sucesso. Saldo atual de R$ {self.saldo:,.2f}')
    
    def __str__(self):
        return f'A conta {self.id} de {self.titular} tem R$ {self.saldo:,.2f} de saldo.'
    
    def depositar(self, valor):
        self.saldo += valor
        print(f'Deposito de R${valor:,.2f} autorizado na conta {self.id}')

    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Saque Negado de R$ {valor:,.2f} na conta {self.id}: SALDO INSUFICIENTE')
        else:
            self.saldo -= valor
            print(f'Saque de R${valor:,.2f} autorizado na conta {self.id}')
    
#Criando o 1° Objeto
c1 = ContaBancaria(111, 'Jose', 500)
inspect(c1) #Inspect visualizar de uma forma melhor oque está dentro do objeto
#print(c1.__getstate__)






