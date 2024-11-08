class Figura:
    def __init__(self, nombre):
        self.nombre = nombre

    def calcular_area(self):
        raise NotImplementedError("El método calcular_area() no está implementado en esta clase.")

class Circulo(Figura):
    def __init__(self, nombre, radio):
        super().__init__(nombre)
        self.radio = radio

    def calcular_area(self):
        return 3.1415 * self.radio ** 2

class Rectangulo(Figura):
    def __init__(self, nombre, base, altura):
        super().__init__(nombre)
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura
figura_1 = Figura("Mi primera figura")
circulo_1 = Circulo("Mi primer círculo", 5)
rectangulo_1 = Rectangulo("Mi primer rectángulo", 2, 4)

try:
    area_figura_1 = figura_1.calcular_area()
    print(area_figura_1)
except NotImplementedError:
    print("El método calcular_area() no está implementado en esta clase.")

try:
    area_circulo_1 = circulo_1.calcular_area()
    print(area_circulo_1)
except NotImplementedError:
    print("El método calcular_area() no está implementado en esta clase.")

try:
    area_rectangulo_1 = rectangulo_1.calcular_area()
    print(area_rectangulo_1)
except NotImplementedError:
    print("El método calcular_area() no está implementado en esta clase.")
