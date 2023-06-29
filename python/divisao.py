# Pedir os valores
# Dividir o primeiro pelo segundo
# Mostrar o resultado

print("Divisão de dois números")
numerador = int(input("Entre com o numerador: "))
denominador = int(input("Entre com o denominador: "))
if denominador == 0:
    print("Não é possível dividir por zero")
    exit()
resultado_da_divisao = numerador / denominador
print("O resultado da divisão é: ", resultado_da_divisao)
