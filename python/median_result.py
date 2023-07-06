# Programa para calcular média
# Pedir o nome aluno
# Pedir a nota 1
# Pedir a nota 2
# Valor da recuperação
# Calcular a média
# calcular o valor da recuperação
# Exibir o resultado e nome do aluno
# Exibir o valor da recuperação

name_student = input("Entre com o nome do aluno: ")
note_1 = float(input("Entre com a nota 1: "))
note_2 = float(input("Entre com a nota 2: "))
recovery = float(input("Entre com o valor da recuperação: "))
avg = (note_1 + note_2) / 2
if avg <= 3:
    print("O aluno ", name_student, " está reprovado")
    print("E o valor da recuperação é: ", recovery + (recovery * 0.1))
elif avg > 3 and avg <= 5:
    print("O aluno ", name_student, " está de recuperação")
    print("E o valor da recuperação é: ", recovery)
    
if avg > 5:
    print("O aluno ", name_student, " está aprovado")
    print("E o valor da recuperação é: ", recovery)
        