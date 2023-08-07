class Veiculo():
    def __init__(self, tipo, chassi, marca, modelo, ano):
        self.tipo = tipo
        self.chasi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
class Motocicleta(Veiculo):
    def __init__(self, tipo,chassi, marca, modelo, ano, cilindrada):
        super().__init__(tipo, chassi, marca, modelo, ano)
        self.cilindrada = cilindrada
        
v = Veiculo('carro', '4d4ad465a46d464d6', 'Ferrari', 'F112','2017')
print(vars(v))
m = Motocicleta('motocicleta', '5a5a6a64d46d6d64a', 'Honda', 'CG', '2008', 150)
print(vars(m))
