print("Resultado das médias das notas")
nome = input("Nome do aluno: ")
nota_unidade1 = float(input("Nota 1ª Unidade: "))
nota_unidade2 = float(input("Nota 2ª Unidade: "))
nota_unidade3 = float(input("Nota 3ª Unidade: "))
nota_unidade4 = float(input("Nota 4ª Unidade: "))

media_do_aluno = (nota_unidade1 + nota_unidade2 + nota_unidade3 + nota_unidade4) / 4

print(nome, ", sua média é {:.2f}".format(media_do_aluno))

if media_do_aluno >= 6:
    print("Aprovado")
else:
    print("Reprovado")
