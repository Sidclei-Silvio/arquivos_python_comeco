# nome do aluno
# nota 1
# nota 2
# calcula a media
# se a media for maior ou igual a 5
# imprime aprovado
# se nao informa reprovado

print("Calculo de média de notas")
student_name = input("Entre com o nome do aluno: ")
note1 = float(input("Entre com a primeira nota: "))
note2 = float(input("Entre com a segunda nota: "))
student_average = (note1 + note2) / 2
if student_average >= 5:
    print(student_name, " sua média é ", student_average)
    print("Aprovado")
else:
    print(student_name, " sua média é ", student_average)
    print("Reprovado")
