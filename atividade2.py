class Ingresso:
    def __init__(self, valor, qnt_disponivel):
        self._valor = valor
        self.qnt_disponivel = qnt_disponivel
    
    def valor_Ingresso(self):
        print(f"O valor do ingresso é: {self._valor}")
    
    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self, valor):
        self._valor = valor
    
    @property
    def qnt_disponivel(self):
        return self._qnt_disponivel
    
    @qnt_disponivel.setter
    def qnt_disponivel(self, qnt_disponivel):
        self._qnt_disponivel = qnt_disponivel

    def comprar(self):
        if(self._qnt_disponivel > 0 ):
            print("Ingresso comprado!!!")
            self.qnt_disponivel -= 1
        else:
            print("Ingressos esgotados")

class VIP(Ingresso):
    def __init__(self, valor, adicional, qnt_disponivel):
        self.valor = valor
        self.adicional = adicional
        super().__init__(qnt_disponivel)

    def valor(self):
        return self.valor + self.adicional

class Ingresso_Normal:
    print("ingresso Normal")

class Camarote_inferior(VIP):
    def __init__(self,valor, adicional, localizacao):
        super().__init__(valor)
        super().__init__(adicional) 
        self.localizacao = localizacao

    @property
    def localizacao(self):
        return self._localizacao
    
    @localizacao.setter
    def localizacao(self, localizacao):
        self._localizacao = localizacao

class Camarote_Superior(VIP):
    def __init__(self,valor, adicional, localizacao):
        super().__init__(valor)
        super().__init__(adicional) 
        self.localizacao = localizacao

    @property
    def localizacao(self):
        return self._localizacao
    
    @localizacao.setter
    def localizacao(self, localizacao):
        self._localizacao = localizacao

def exibir_ingressos(Ingresso_Normal_Function, Camarote_inferior_Function, Camarote_superior_Function):
    print(f"""+--------------------------------------------------------------+
Ingressos normais disponiveis: {Ingresso_Normal_Function.qnt_disponivel()}""")
    for i in range(0, Camarote_inferior_Function.len()):
        print(f"Camarote Inferior | Valor: {Camarote_inferior_Function[i].valor} | Quantidade Disponivel: {Camarote_inferior_Function[i].qnt_disponivel}")
    for j in range(0, Camarote_superior_Function.len()):
        print(f"Camarote Inferior | Valor: {Camarote_superior_Function[i].valor} | Quantidade Disponivel: {Camarote_superior_Function[i].qnt_disponivel}")
    print("+--------------------------------------------------------------+")

Ingresso_Normal = []
Camarote_inferior = []
Camarote_superior = []
encerrar = 4
encerrar1 = 0

while(encerrar != 0):
    Ingresso_Normal = Ingresso(int(input("Digite o valor do ingresso normal: ")), int(input("Digite a quantidade deste ingressos disponivel: ")))
    print(Ingresso_Normal._valor)
    Camarote_inferior.append(Camarote_inferior(Ingresso_Normal.valor, int(input("Digite o acressimo do valor no ingresso vip: ")),  int(input("Digite a localizacao deste ingressos: "))))
    Camarote_Superior.append(Camarote_Superior(Camarote_inferior.valor, int(input("Digite o acressimo do valor no camarote superior: ")), int(input("Digite a localizacao deste ingressos: "))))
    encerrar == 1
    while(encerrar == 1):
        encerrar = int(input(("""+------------------------------------+
|2-Comprar                           |
|3-Ingressos disponiveis             |
|4- Adicionar Igresso                |
+------------------------------------+
""")))
    while(encerrar == 2):
        exibir_ingressos(Ingresso_Normal, Camarote_inferior, Camarote_Superior)
        encerrar1 = int(input(("""+-----------------------+
|1-Ingresso normal      |
|2-Camarote inferior    |
|3-Camarote superior    |
+-----------------------+
""")))
        while(encerrar1 == 1):
            Ingresso_Normal.comprar()
        
        while(encerrar1 == 2):
            Camarote_inferior.comprar()
        
        while(encerrar1 == 3):
            Camarote_Superior.comprar()
        encerrar = 1
    while(encerrar == 3):
        exibir_ingressos(Ingresso_Normal, Camarote_inferior, Camarote_Superior)
    while(encerrar == 4):
        encerrar1 = int(input(("""+-----------------------+
|1-Ingresso normal      |
|2-Camarote inferior    |
|3-Camarote superior    |
+-----------------------+
""")))
        while(encerrar1 == 1):
            Ingresso_Normal = Ingresso(int(input("Digite o valor do ingresso normal: ")), int(input("Digite a quantidade deste ingressos disponivel: ")))
        
        while(encerrar1 == 2):
            Camarote_inferior.append(Camarote_inferior(int(input("Digite o valor do ingresso normal: ")),  int(input("Digite a localizacao deste ingressos: "))))
        
        while(encerrar1 == 3):
            Camarote_Superior.append(Camarote_Superior(int(input("Digite o valor do ingresso normal: ")), int(input("Digite o valor do acrecimo: ")), int(input("Digite a localizacao deste ingressos: "))))