class Pessoa:
    def __init__(self, nome, sexo, idade) -> None:
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
    def falar(self):
        print ("Estou falando")        
    
aluno1 = Pessoa("Pedro", "Masculino", 25)
aluno2 = Pessoa("Silvia", "Feminino", 24)
professor = Pessoa("Paulo", "Masculino", 79)
print (aluno1.nome)
print (aluno2.nome)
aluno2.falar()
