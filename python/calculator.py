# Função soma
# Pega o primeiro valor
# Pega o segundo valor
# E Retorna a soma dos dois valores
def soma(valor1, valor2):
    return valor1 + valor2


# Função subtração
def sub(valor1, valor2):
    return valor1 - valor2


# Função Multiplicação
def mult(valor1, valor2):
    return valor1 * valor2


# Função Divisão
def div(valor1, valor2):
    return valor1 / valor2


def main():
    operacao = input("Digite o símbolo da operação desejada (+,-,/,*)")
    valor1 = float(input("Entre com o primero valor "))
    valor2 = float(input("Entre com o segundo valor "))
    if operacao == "+":
        return soma(valor1, valor2)
    if operacao == "-":
        return sub(valor1, valor2)
    if operacao == "/":
        return div(valor1, valor2)
    if operacao == "*":
        return mult(valor1, valor2)


result = main()
print(result)
