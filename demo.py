class cuadrado:
    def __init__(self,lado):
        self.lado = lado

    def area(self):
         self.lado * self.lado

NumLado = cuadrado (5)
print("El resultado es:",NumLado.lado)