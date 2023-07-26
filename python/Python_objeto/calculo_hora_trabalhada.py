class Funcionario:
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.__salario = 0  # private
        self.__horas_trabalhadas = 0  # private

    @property
    def salario(self):
        return self.__salario

    def registra_hora_trabalhada(self, horas):
        self.__horas_trabalhadas += horas

    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada
        return self.__salario


jose = Funcionario("José", "Professor", 50)

# Vamos supor que José trabalhou 8 horas em um dia e 6 horas em outro dia.
jose.registra_hora_trabalhada(8)
jose.registra_hora_trabalhada(6)

# Agora, calculamos o salário com base nas horas trabalhadas registradas.
print(
    jose.calcula_salario()
)  # O salário será calculado com base nas horas trabalhadas (8 + 6) e no valor da hora (50).
