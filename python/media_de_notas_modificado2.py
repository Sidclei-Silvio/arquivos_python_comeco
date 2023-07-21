print("Resultado das médias das notas")
nome = input("Nome do aluno: ")
nota_unidade1 = float(input("Nota 1ª Unidade: "))
nota_unidade2 = float(input("Nota 2ª Unidade: "))
nota_unidade3 = float(input("Nota 3ª Unidade: "))
nota_unidade4 = float(input("Nota 4ª Unidade: "))
media_do_aluno = (nota_unidade1 + nota_unidade2 + nota_unidade3 + nota_unidade4) / 4
if media_do_aluno >= 6:
  print(nome, "sua média é ", media_do_aluno)
  print("Aprovado")
else:
  print(nome, "sua média é ", media_do_aluno)
  print("Reprovado")