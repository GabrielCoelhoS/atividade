class Forma():
    print("Teste")
    def __init__(self, lado):
        self._lado = lado
    
    @property
    def lado(self):
        return self._lado
    
    @lado.setter
    def lado(self, lado):
        self._lado = lado

    def dados(self):
        print("Area = ", self.lado**2, "Perimetro", self.lado*4 )

class Retangulo(Forma):
    def __init__(self, lado, altura):
        super().__init__(lado)
        self._altura = altura
    
    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, altura):
        self._altura = altura

    def dados(self):
        print("Area = ", (self.lado*self.altura), "Perimetro", self.lado * 2 + 2 * self.altura)

class Triangulo(Forma):
    def __init__(self, lado, altura):
        super().__init__(lado)
        self._altura = altura
    
    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, altura):
        self._altura = altura

    def dados(self):
        print("Area = ", (self.lado*self.altura)/2, "Perimetro", self.lado * 2  +  self.altura)

encerrar = 1
contador = [0,0,0]
quadrados = []
retangulos = []
triangulos = []

while (encerrar !=0):
    while(encerrar == 1):
        encerrar = int(input("""+-----------------------+
|2- Quadrado            |
|3- Retangulo           |
|4- Triangulo           |
|0- Encerrar            |
+-----------------------+
"""))
    while(encerrar == 2):
        quadrados.append(Forma(int(input("Digite o valor dos lados do quadrado: "))))
        quadrados[contador[encerrar-2]].dados()
        contador[encerrar-2] += 1
        encerrar = int(input("""+-----------------------+
|1- Menu                |
|2- Continuar           |
+-----------------------+
"""))
    
    while(encerrar == 3):
        retangulos.append(Retangulo(int(input("Digite o valor dos lados do retangulo: ")),int(input("Digite o valor da altura do retangulo: "))))
        retangulos[contador[encerrar-2]].dados()
        contador[encerrar-2] += 1
        encerrar = int(input("""+-----------------------+
|1- Menu                |
|3- Continuar           |
+-----------------------+
"""))
    
    while(encerrar == 4):
        triangulos.append(Triangulo(int(input("Digite o valor dos dois lados iguais do triangulo: ")),int(input("Digite o valor do outro lado do triangulo: "))))
        triangulos[contador[encerrar-2]].dados()
        contador[encerrar-2] += 1
        encerrar = int(input("""+-----------------------+
|1- Menu                |
|4- Continuar           |
+-----------------------+
"""))