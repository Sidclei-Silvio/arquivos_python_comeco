def get_student_name():
    """Obtém o nome do aluno."""
    name = input("Entre com o nome do aluno: ")
    return name


def get_student_grade(grade_number):
    """Obtém a nota de um aluno."""
    grade = float(input(f"Entre com a nota {grade_number}: "))
    return grade


def get_recovery_value():
    """Obtém o valor da recuperação."""
    recovery = float(input("Entre com o valor da recuperação: "))
    return recovery


def calculate_average(grade_1, grade_2):
    """Calcula a média das notas."""
    avg = (grade_1 + grade_2) / 2
    return avg


def get_student_status(avg):
    """Determina o status do aluno com base na média."""
    if avg <= 3:
        return "reprovado"
    elif avg <= 5:
        return "de recuperação"
    else:
        return "aprovado"


def adjust_recovery_value(avg, recovery):
    """Ajusta o valor da recuperação, se necessário."""
    if avg <= 3:
        recovery += recovery * 0.1
    return recovery


def display_result(name, status, recovery=None):
    """Exibe o resultado e o nome do aluno."""
    print(f"O aluno {name} está {status}")
    if recovery is not None:
        print(f"E o valor da recuperação é: {recovery}")


def main():
    """Função principal do programa."""
    # Pedir o nome do aluno
    name_student = get_student_name()

    # Pedir as notas
    note_1 = get_student_grade(1)
    note_2 = get_student_grade(2)

    # Pedir o valor da recuperação
    recovery = get_recovery_value()

    # Calcular a média
    avg = calculate_average(note_1, note_2)

    # Ajustar o valor da recuperação, se necessário
    recovery = adjust_recovery_value(avg, recovery)

    # Calcular o status do aluno
    status = get_student_status(avg)

    # Exibir o resultado e o nome do aluno
    display_result(name_student, status, recovery)


if __name__ == "__main__":
    main()
