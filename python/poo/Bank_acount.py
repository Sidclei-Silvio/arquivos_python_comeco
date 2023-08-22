class Bank_acount:
    def __init__(self, acount_number, balance = 0):
        self.balance = balance
        self.acount_number = acount_number
    def deposit(self, cash):
        if cash > 0:
            self.balance += cash
            print (f"Depósito de {cash} realizado. Saldo atual: {self.balance}")
        else:
            print ("Valor inválido")
    def withdraw(self, cash):
        if cash <= self.balance:
            self.balance -= cash
            print (f"Saque de {cash} realizado. Saldo atual: {self.balance}")
        else:
            print ("Saldo insuficiente")    
            
Bradesco = Bank_acount ("023468-2", 10.00)
print (Bradesco.balance)
Bradesco.deposit(1000)
print(Bradesco.balance)
Bradesco.deposit(-20)
Bradesco.withdraw(500)
Bradesco.withdraw(600)


# Caixa = Bank_acount ("225458-8")
# print(Caixa.balance)
# Caixa.deposit(2000)


