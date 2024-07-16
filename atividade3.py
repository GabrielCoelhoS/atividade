class Veiculo: 
    def __init__(self,preco , modelo ):
        self._preco = preco
        self._modelo = modelo

    @property
    def preco(self):
        return self.preco
    
    @preco.setter
    def preco(self, preco):
        self._preco = preco

    @property
    def modelo(self):
        return self.modelo
    
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

class Carro(Veiculo):
    def __init__(self,preco, modelo, Km):
        super().__init__(preco)
        super().__init__(modelo)
        self._km = Km
    
    @property
    def km(self):
        return self.km
    
    @km.setter
    def km(self, km):
        self._km = km

    def Reajuste(self):
        if(self.km > 100000):
            self.valor *= 0.92

class Moto(Veiculo):
    def __init__(self,preco, modelo, ano):
        super().__init__(preco)
        super().__init__(modelo)
        self._ano = ano
    
    @property
    def ano(self):
        return self.ano
    
    @ano.setter
    def ano(self, ano):
        self._ano = ano

    def Reajuste(self):
        if(self.ano >= 2008):
            return self.preco * 1.1

encerrar = 1 
encerrar1 = 0
Carros = []
Motos = []
while(encerrar != 0):
    while(encerrar == 1):
        encerrar1 = input(int(("""+-----------------+
|1- Carro         |
|2- Moto          |
+-----------------+""")))
        if (encerrar1 == 1):
            preco = int(input("Digite o preço do carro: "))
            while(preco <= 0):
                print("Valor invalido!!!!")
                preco = int(input("Digite o preço do carro: "))
            modelo = int(input("Digite o preço do carro: "))
            km = int(input("Digite a quantidade de km do carro: "))
            while(km <= 0):
                print("Valor invalido!!!!")
                km = int(input("Digite a quantidade de km carro: "))
            Carros.append(Carro(preco, modelo, km))
        else:
            preco = int(input("Digite o preço do carro: "))
            while(preco <= 0):
                print("Valor invalido!!!!")
                preco = int(input("Digite o preço do carro: "))
            modelo = int(input("Digite o preço do carro: "))
            ano = int(input("Digite a quantidade de km do carro: "))
            while(ano < 1885 or ano > 2025):
                print("Valor invalido!!!!")
                km = int(input("Digite a quantidade de km carro: "))
            Motos.append(Carro(preco, modelo, ano))
    
    while(encerrar == 2):
        print("Tipo | Preço | Modelo | KM ou Ano | Preço reajustado")
        for i in range(0, Carros.append()):
                print(f"Carro | {Carros[i].preco} | {Carros[i].modelo} | {Carros[i].km} | {Carros[i].Reajuste(Carros[i])} ")
        
        for i in range(0, Motos.append()):
                print(f"Moto | {Motos[i].preco} | {Motos[i].modelo} | {Motos[i].km} | {Motos[i].Reajuste(Motos[i])} ")