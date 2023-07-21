# Solicitar ao usuário o preço do produto e a quantidade desejada
preco_produto = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade desejada: "))

# Calcular o valor total
valor_total = preco_produto * quantidade

# Exibir o valor total
print("O valor total a ser pago é R$ {:.2f}".format(valor_total))