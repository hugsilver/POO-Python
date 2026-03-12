from rich.traceback import install
install() #Fica monitorado pela biblioteca do traceback

def divisão(x, y):
    return x/y

print(divisão(50/0))