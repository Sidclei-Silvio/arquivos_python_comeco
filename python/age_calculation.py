# Pede data do nascimento
# Pede data atual
# Armazenar em uma variavel a idade da pessoa
# Exibir a idade da pessoa

print("Esse programa calcula a idade de uma pessoa")
date_of_birth = int(input("Entre com o ano de nascimento: "))
current_date = int(input("Entre com o ano atual: "))
age_of_person = current_date - date_of_birth
print("Sua idade é: ", age_of_person, " anos")
if age_of_person >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")
