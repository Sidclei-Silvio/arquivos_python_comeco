# Primeira função
# Uma função é um bloco de código que pode ser chamado em qualquer parte do programa.


# Função somar


# Pegar o primeiro número
# Pegar o segundo número
# Somar os dois números
# Exibir o resultado da soma


def sum_two_numbers():
    first_number = int(input("Entre com o primeiro número: "))
    second_number = int(input("Entre com o segundo número: "))
    sum_of_numbers = first_number + second_number
    return "A soma dos números é: ", sum_of_numbers


# Função subtrair
def subtract_two_numbers():
    first_number = int(input("Entre com o primeiro número: "))
    second_number = int(input("Entre com o segundo número: "))
    subtraction_of_numbers = first_number - second_number
    return "A subtração dos números é: ", subtraction_of_numbers


# Função com parametro
def sum_two_numbers_with_parameter(first_number, second_number):
    return first_number + second_number


# Função para subtrair com parametro
def subtract_two_numbers_with_parameter(first_number, second_number):
    return first_number - second_number


# Função para pedir os números
def ask_for_two_numbers():
    first_number = int(input("Entre com o primeiro número: "))
    second_number = int(input("Entre com o segundo número: "))
    return first_number, second_number


# Função para exibir o resultado
def show_result(result):
    print("O resultado é: ", result)


print("Cálculo de idade")
a, b = ask_for_two_numbers()
print("a sua idade é o resultado abaixo")
show_result(subtract_two_numbers_with_parameter(a, b))
