# Calculo de media
# Pedir o total de alunos
# Pedir o total das unidades
# Pedir o total de notas
# O programar vai de acordo com o total de unidades, alunos e notas ele imprime a media de cada aluno

print("Cálculo de média")
number_of_students = int(input("Digite o total de alunos: "))
number_of_units = int(input("Digite o total de unidades: "))

for i in range(number_of_students):
    total_grade = 0.0  # Corrigido para float
    for j in range(number_of_units):
        grade = float(input(f"Digite a nota {j+1} do aluno {i+1}: "))
        total_grade += grade
    avg = total_grade / number_of_units
    print(f"A média do aluno {i+1} é: {avg}")
