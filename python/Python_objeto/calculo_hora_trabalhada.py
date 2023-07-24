class Funcionario():
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.__salario = 0  # private
        self.__horas_trabalhadas = 0  # private
        
    @property
    def salario(self):
        return self.__salario
    
    def registra_hora_trabalhada(self):
        self.__horas_trabalhadas += 1
        
    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada
        return self.__salario

jose = Funcionario('José', 'Professor', 50)
jose.registra_hora_trabalhada()
jose.registra_hora_trabalhada()
jose.registra_hora_trabalhada()
print(jose.calcula_salario())  # O salário será calculado com base nas horas trabalhadas (3) e no valor da hora (50).
