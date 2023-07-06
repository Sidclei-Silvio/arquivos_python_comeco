nome = ["Sidney", "João", "Maria", "José"]


for i in nome:
    print(i)


for i in range(5):
    try:
        print(nome[i])
    except IndexError:
        print("Não existe esse índice na lista")
