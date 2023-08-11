class Car:
    def __init__(self, brand, model, color, fuel, speed):
        self.brand = brand
        self.model = model
        self.color = color
        self.fuel = fuel
        self.speed = speed

    def speed_up(self, value=1):
        self.speed += value

    def speed_down(self):
        self.speed -= 1

    def stop(self):
        self.speed = 0

    def __str__(self):
        return '{} {} {} {} {}'.format(self.brand, self.model, self.color, self.fuel, self.speed)
    
ecosport = Car('Ford', 'Ecosport', 'Blue', 'Gasoline', 0)    
spin = Car('Chevrolet', 'Spin', 'White', 'Gasoline', 0)

ecosport.speed_up(100)
spin.speed_up()
spin.speed_up()
spin.speed_down()
print(ecosport)
print(spin)