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
c1 = ContaBancaria(112, 'Gustavo', 3000)
c1.depositar(500)
c1.sacar(2_000_000) #2 milhões
print(c1)
#print(c1.__doc__)

#OBS: Uso de prints dentro de classes não é tão recomendavel, idela usar o return


