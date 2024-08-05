class Class_Livro:
    def __init__(self, Titulo_Atributo, Autor_Atributo, Ano_Publicacao_Atributo, Disponibilidade_Atributo):
        self._Titulo_Atributo = Titulo_Atributo
        self._Autor_Atributo = Autor_Atributo
        self._Ano_Publicacao_Atributo = Ano_Publicacao_Atributo
        self._Disponibilidade_Atributo = Disponibilidade_Atributo
    
    @property
    def Titulo_Atributo(self):
        return self._Titulo_Atributo

    @Titulo_Atributo.setter
    def Titulo_Atributo(self, Titulo_Atributo):
        self._Titulo_Atributo = Titulo_Atributo
    @property
    def Autor_Atributo(self):
        return self._Autor_Atributo
    
    @Autor_Atributo.setter
    def Autor_Atributo(self, Autor_Atributo):
        self._Autor_Atributo = Autor_Atributo
    
    @property
    def Ano_publicacao_Atributo(self):
        return self._Ano_Publicacao_Atributo
    
    @Ano_publicacao_Atributo.setter
    def Ano_publicacao_Atributo(self, Ano_publicacao_Atributo):
        self._Ano_publicacao_Atributo = Ano_publicacao_Atributo
    
    @property
    def Disponibilidade_Atributo(self):
        return self._Disponibilidade_Atributo
    
    @Disponibilidade_Atributo.setter
    def Disponibilidade_Atributo(self, Disponibilidade_Atributo):
        self._Disponibilidade_Atributo = Disponibilidade_Atributo

    def Function_Emprestar_Livros_Class_Livro(self):
        if self._Disponibilidade_Atributo:
            self._Disponibilidade_Atributo = False
    
    def Function_Devolver_Livro_Class_Livro(self):
        self._Disponibilidade_Atributo = True

    def Function_Exibir_Informacoes(self):
        print(f"""Titulo: {self.Titulo_Atributo} | Autor: {self.Autor_Atributo} | Ano de Publicação: {self.Ano_publicacao_Atributo} | Disponibilidade: {self.Disponibilidade_Atributo}""")

class Class_User:
    def __init__(self, Nome_User_Atributo, Livros_Emprestados_User_Atributo = []):
        self._Nome_User_Atributo = Nome_User_Atributo
        self._Livros_Emprestados_User_Atributo = Livros_Emprestados_User_Atributo
    
    @property
    def Nome_User_Atributo(self):
        return self._Nome_User_Atributo
    
    @property
    def Livros_Emprestados_User_Atributo(self):
        return self._Livros_Emprestados_User_Atributo
    
    @Livros_Emprestados_User_Atributo.setter
    def Livros_Emprestados_User_Atributo(self, Livros_Emprestados_User_Atributo = []):
        self._Livros_Emprestados_User_Atributo = Livros_Emprestados_User_Atributo

    
    def Function_Emprestar_Livros_Class_User(self, Objeto_Livro_Atributo):
        if Objeto_Livro_Atributo.Disponibilidade_Atributo:
            Livros_Emprestados_User_Atributo_Auxiliar = self.Livros_Emprestados_User_Atributo
            Objeto_Livro_Atributo.Function_Emprestar_Livros_Class_Livro()
            self.Livros_Emprestados_User_Atributo(Livros_Emprestados_User_Atributo_Auxiliar.append(Objeto_Livro_Atributo))
            return True
        else:
            return False
        
    def Function_Devolver_Livro_Class_User(self, Objeto_Livro_Devolvido_Atributo):
        i = 0
        while True:
            if self.Livros_Emprestados_User_Atributo[i] == Objeto_Livro_Devolvido_Atributo:
                Livros_Emprestados_User_Atributo_Auxiliar = self.Livros_Emprestados_User_Atributo
                del Livros_Emprestados_User_Atributo_Auxiliar[i]
                Livros_Emprestados_User_Atributo_Auxiliar.sort()
                Objeto_Livro_Devolvido_Atributo.Function_Delvolver_Livro_Class_Livro()
                self.Livros_Emprestados_User_Atributo(Livros_Emprestados_User_Atributo_Auxiliar)
                break
            else:
                i += 1

    def Function_Exibir_Livros_Emprestados(self):
        for i in range(0, self.Livros_Emprestados_User_Atributo.__len__()):
            self.Livros_Emprestados_User_Atributo[i].Function_Exibir_Informacoes()
    
    def Function_Buscar_Titulo_Livro_Emprestado(self, Titulo_Buscado):
        contador = 0
        while contador <= self.Livros_Emprestados_User_Atributo.__len__():
            if self.Livros_Emprestados_User_Atributo[contador].Titulo_Atributo == Titulo_Buscado:
                return self.Livros_Emprestados_User_Atributo[contador] #Pode não parar o while
            else:
                contador += 1
    
    def Function_Buscar_Autor_Livro_Emprestado(self, Autor_Buscado):
        contador = 0
        while contador <= self.Livros_Emprestados_User_Atributo.__len__():
            if self.Livros_Emprestados_User_Atributo[contador].Autor_Atributo == Autor_Buscado:
                print("Livro encontrado!!")
                return self.Livros_Emprestados_User_Atributo[contador]
            else:
                print("Livro não encontrado!!")
            contador += 1

class Class_Funcionario(Class_User):
    def __init__(self, Nome_Fucionario_Atributo, ID_Funcionario_Atributo, Cargo_Funcionario_Atributo, Livros_Emprestados_Fucionario_Atributo = []):
        super().__init__(Nome_Fucionario_Atributo, Livros_Emprestados_Fucionario_Atributo)
        self._ID_Funcionario_Atributo = ID_Funcionario_Atributo
        self._Cargo_Funcionario_Atributo = Cargo_Funcionario_Atributo
    
    @property
    def ID_Funcionario_Atributo(self):
        return self._ID_Funcionario_Atributo
    
    @property
    def Cargo_Funcionario_Atributo(self):
        return self._Cargo_Funcionario_Atributo
    
    @Cargo_Funcionario_Atributo.setter
    def Cargo_Funcionario_Atributo(self, Cargo_Funcionario_Atributo = []):
        self._Cargo_Funcionario_Atributo = Cargo_Funcionario_Atributo

    def Function_Adicionar_Livro(self, Titulo_Class_Funcionario_Atributo, Autor_Class_Funcionario_Atributo, Ano_Publicacao_Class_Funcionario_Atributo, Disponibilidade_Class_Funcionario_Atributo):
        Objeto_Livro_Temporario = Class_Livro(Titulo_Class_Funcionario_Atributo, Autor_Class_Funcionario_Atributo, Ano_Publicacao_Class_Funcionario_Atributo, Disponibilidade_Class_Funcionario_Atributo)
        return Objeto_Livro_Temporario
    
    def Function_Deletar_Livro(self, Lista_Livros_Atributo, Posicao_Livro_Atributo):
        del Lista_Livros_Atributo[Posicao_Livro_Atributo]
        return Lista_Livros_Atributo
    
    def Function_Editar_Livro(Objeto_Livro_Antigo, Novo_Titulo_Atributo, Novo_Autor_Atributo, Novo_Ano_Publicacao_Atributo):
        Objeto_Livro_Antigo.Titulo_Atributo(Novo_Titulo_Atributo)
        Objeto_Livro_Antigo.Autor_Atributo(Novo_Autor_Atributo)
        Objeto_Livro_Antigo.Ano_Publicacao_Atributo(Novo_Ano_Publicacao_Atributo)

class Class_Biblioteca:
    def __init__(self, Lista_Livros_Atributo = [], Lista_User_Atributo = []):
        self._Lista_Livros_Atributo = Lista_Livros_Atributo
        self._Lista_User_Atributo = Lista_User_Atributo

    @property
    def Lista_Livros_Atributo(self):
        return self._Lista_Livros_Atributo
    
    @Lista_Livros_Atributo.setter
    def Lista_Livros_Atributo(self, Lista_Livros_Atributo = []):
        self._Lista_Livros_Atributo = Lista_Livros_Atributo

    @property
    def Lista_User_Atributo(self):
        return self._Lista_User_Atributo
    
    @Lista_User_Atributo.setter
    def Lista_User_Atributo(self, Lista_User_Atributo = []):
        self._Lista_User_Atributo = Lista_User_Atributo

    def Function_Add_User(self, Nome_User_Atributo, Livros_Emprestados_User_Atributo):
        Object_User_Temp = Class_User(Nome_User_Atributo, Livros_Emprestados_User_Atributo)
        self.Lista_User_Atributo.append(Object_User_Temp)
    
    def Function_Remove_User(self, Posicao_User_Atributo):
        del self.Lista_User_Atributo[Posicao_User_Atributo]
        
    def Function_Buscar_Titulo(self, Titulo_Buscado):
        contador = 0
        while contador <= self.Lista_Livros_Atributo.__len__():
            if self.Lista_Livros_Atributo[contador].Titulo_Atributo == Titulo_Buscado:
                Encontrado_Function = True
                Object_Livro_Encotrado = self.Lista_Livros_Atributo[contador]
                break
            contador += 1
        return Object_Livro_Encotrado, Encontrado_Function, contador
    
    def Function_Buscar_Autor(self, Autor_Buscado):
        contador = 0
        while contador <= self.Lista_Livros_Atributo.__len__():
            if self.Lista_Livros_Atributo[contador].Titulo_Atributo == Autor_Buscado:
                Encontrado_Function = True
                Object_Livro_Encotrado = self.Lista_Livros_Atributo[contador]
                break
            contador += 1
        return Object_Livro_Encotrado, Encontrado_Function, contador

def Function_Buscar_Autor_Global(Object_Biblioteca_Buscada_Atributo):
    if Object_Biblioteca_Buscada_Atributo.Lista_Livros_Atributo != None:     
        while True:
            Autor_Buscado = str(input("Digite o autor do livro: "))
            Return_Function_Buscar = Object_Biblioteca_Buscada_Atributo.Function_Buscar_Autor(Autor_Buscado)

            while Return_Function_Buscar[1]:
                Return_Function_Buscar[0].Function_Exibir_Informacoes
                Menu_Emprestar_Livro_Function = int(input("""
            +------------------------------+
            1- Buscar outro
            3- Pegar emprestado
            4- Voltar
            +------------------------------+"""))
                if Menu_Emprestar_Livro_Function != 1 and Menu_Emprestar_Livro_Function != 3 and Menu_Emprestar_Livro_Function != 4:
                    print("Numero invalido")
                else:
                    break
                
            if Return_Function_Buscar == False:
                print("Livro não encontrado!!")
                break
        Return_Function_Buscar[2] = Menu_Emprestar_Livro_Function
        return Return_Function_Buscar
    else:
        print("Nenhum Livro cadastrado!")

def Function_Buscar_Titulo_Global(Object_Biblioteca_Buscada_Atributo):
    if Object_Biblioteca_Buscada_Atributo.Lista_Livros_Atributo != None:        
        while True:
            Titulo_Buscado = str(input("Digite o Titulo do livro: "))
            Return_Function_Buscar = Object_Biblioteca_Buscada_Atributo.Function_Buscar_Titulo(Titulo_Buscado)

            while Return_Function_Buscar[1]:
                Return_Function_Buscar[0].Function_Exibir_Informacoes
                Menu_Emprestar_Livro_Function = int(input("""
            +------------------------------+
            1- Buscar outro
            3- Pegar emprestado
            4- Voltar
            +------------------------------+"""))
                if Menu_Emprestar_Livro_Function != 1 and Menu_Emprestar_Livro_Function != 3 and Menu_Emprestar_Livro_Function != 4:
                    print("Numero invalido")
                else:
                    break
                
            if Return_Function_Buscar == False:
                print("Livro não encontrado!!")
                break
        Return_Function_Buscar[2] = Menu_Emprestar_Livro_Function
        return Return_Function_Buscar
    else:
        print("Nenhum Livro cadastrado!")

def Function_Opcoes_User_And_Funcionario(Object_User_Atributo, Object_Biblioteca_Buscada_Atributo):
    Menu_Opcoes_User = 4
    while Menu_Opcoes_User != 0:
        
        if Menu_Opcoes_User == 4:
            Menu_Emprestar_Livro = 4
            Menu_Opcoes_User = int(input("""
+------------------------------+
 1-Pegar livro emprestado
 2-Devolver Livro
 3-Ver livros pegos
 0-Sair
+------------------------------+
"""))
        
        if Menu_Opcoes_User == 1 and Menu_Emprestar_Livro != 0:
            
            if Menu_Emprestar_Livro == 4:
                Menu_Emprestar_Livro = int(input("""
+------------------------------+
1- Buscar por titulo
2- Buscar por autor
0- Sair
+------------------------------+"""))
            
            if Menu_Emprestar_Livro == 1:
                Return_Function_Buscar_Function_O_U = Function_Buscar_Titulo_Global(Object_Biblioteca_Buscada_Atributo)
                Menu_Emprestar_Livro = Return_Function_Buscar_Function_O_U[2]

            if Menu_Emprestar_Livro == 2:
                Return_Function_Buscar_Function_O_U = Function_Buscar_Autor_Global(Object_Biblioteca_Buscada_Atributo)
                Menu_Emprestar_Livro = Return_Function_Buscar_Function_O_U[2]
            
            if Menu_Emprestar_Livro == 3:

                Emprestado = Object_User_Atributo.Function_Emprestar_Livros_Class_User(Return_Function_Buscar_Function_O_U[0])
                if Emprestado:
                    print("Livro emprestado com sucesso!")
                else:
                    print("Livro indisponivel")
                Menu_Emprestar_Livro = 4

            else:
                print("Numero invalido!!!")
                Menu_Emprestar_Livro = 4

        if Menu_Opcoes_User == 2 and Menu_Emprestar_Livro != 0:
            
            if Menu_Emprestar_Livro == 4:
                Menu_Emprestar_Livro = int(input("""
+------------------------------+
1- Buscar por titulo
2- Buscar por autor
0- Sair
+------------------------------+"""))
            
            if Menu_Emprestar_Livro == 1:
                Return_Function_Buscar_Function_O_U = Function_Buscar_Titulo_Global(Object_Biblioteca_Buscada_Atributo)
                Menu_Emprestar_Livro  = Return_Function_Buscar_Function_O_U[2]

            if Menu_Emprestar_Livro == 2:
                Return_Function_Buscar_Function_O_U = Function_Buscar_Autor_Global(Object_Biblioteca_Buscada_Atributo)
                Menu_Emprestar_Livro = Return_Function_Buscar_Function_O_U[2]

            if Menu_Emprestar_Livro == 3:

                Emprestado = Object_User_Atributo.Function_Emprestar_Livros_Class_User(Return_Function_Buscar_Function_O_U[0])
                if Emprestado:
                    print("Livro emprestado com sucesso!")
                else:
                    print("Livro indisponivel")
                Menu_Emprestar_Livro = 4    

            else:
                print("Numero Invalido!!!")
                Menu_Emprestar_Livro = 4

        if Menu_Opcoes_User == 3:
            
            for i in range(0, Object_User_Atributo.Livros_Emprestados_User_Atributo.__len__()):
                Object_User_Atributo.Livros_Emprestados_User_Atributo[i].Function_Exibir_Informacoes
            Menu_Opcoes_User = 4
       
        else: 
            print("Numero invalido!!!")
            Menu_Opcoes_User = 4

def Function_Opcoes_Funcionarios(Object_Funcionario_Atributo, Object_Biblioteca_Buscada_Atributo):
    Menu_Opcoes_Funcionario = 7
    while Menu_Opcoes_Funcionario != 0:
        
        if Menu_Opcoes_Funcionario == 7:
            Menu_Emprestar_Livro = 4
            Menu_Opcoes_Funcionario = int(input("""
+------------------------------+
 1-Pegar livro emprestado
 2-Devolver Livro
 3-Ver livros emprestados
 4-Adicionar livro
 5-Deletar livro
 6-Editar livro
 0-Sair
+------------------------------+
"""))
        
        if Menu_Opcoes_Funcionario == 1 and Menu_Emprestar_Livro != 0:
            
            if Menu_Emprestar_Livro == 4:
                Menu_Emprestar_Livro = int(input("""
+------------------------------+
1- Buscar por titulo
2- Buscar por autor
0- Sair
+------------------------------+"""))
            
            if Menu_Emprestar_Livro == 1:
                Return_Function_Buscar_Function_O_F = Function_Buscar_Titulo_Global(Object_Biblioteca_Buscada_Atributo)
                Menu_Emprestar_Livro = Return_Function_Buscar_Function_O_F[2]

            if Menu_Emprestar_Livro == 2:
                Return_Function_Buscar_Function_O_F = Function_Buscar_Autor_Global(Object_Biblioteca_Buscada_Atributo)
                Menu_Emprestar_Livro = Return_Function_Buscar_Function_O_F[2]
            
            if Menu_Emprestar_Livro == 3:

                Emprestado = Object_Funcionario_Atributo.Function_Emprestar_Livros_Class_User(Return_Function_Buscar_Function_O_F[0])
                if Emprestado:
                    print("Livro emprestado com sucesso!")
                else:
                    print("Livro indisponivel")
                Menu_Emprestar_Livro = 4
        
        if Menu_Opcoes_Funcionario == 2 and Menu_Emprestar_Livro != 0:
            
            if Menu_Emprestar_Livro == 4:
                Menu_Emprestar_Livro = int(input("""
+------------------------------+
1- Buscar por titulo
2- Buscar por autor
0- Sair
+------------------------------+"""))
            
            if Menu_Emprestar_Livro == 1:
                Return_Function_Buscar_Function_O_F = Function_Buscar_Titulo_Global(Object_Biblioteca_Buscada_Atributo)
                Menu_Emprestar_Livro = Return_Function_Buscar_Function_O_F[2]

            if Menu_Emprestar_Livro == 2:
               Return_Function_Buscar_Function_O_F = Function_Buscar_Autor_Global(Object_Biblioteca_Buscada_Atributo)
               Menu_Emprestar_Livro = Return_Function_Buscar_Function_O_F[2]

            if Menu_Emprestar_Livro == 3:

                Emprestado = Object_Funcionario_Atributo.Function_Emprestar_Livros_Class_User(Return_Function_Buscar_Function_O_F[0])
                if Emprestado:
                    print("Livro emprestado com sucesso!")
                else:
                    print("Livro indisponivel")
                Menu_Emprestar_Livro = 4    
        
        if Menu_Opcoes_Funcionario == 3:
            
            for i in range(0, Object_Funcionario_Atributo.Livros_Emprestados_Funcionario_Atributo.__len__()):
                Object_Funcionario_Atributo.Livros_Emprestados_Funcionario_Atributo[i].Function_Exibir_Informacoes

        if Menu_Opcoes_Funcionario == 4:
            Titulo_Livro_Temp = str(input("Digite o titulo do livro: "))
            Autor_Livro_Temp = str(input("Digite o autor do livro: "))
            Ano_Publicacao_Livro_Temp = int(input("Digite o ano de publicação do livro: "))
            while Ano_Publicacao_Livro_Temp < 0 and Ano_Publicacao_Livro_Temp > 2024:
                print("Ano de lancamento invalido!!!")
                Ano_Publicacao_Livro_Temp = int(input("Digite o ano de publicação do livro: "))
            Object_Livro_Temp = Class_Livro(Titulo_Livro_Temp, Autor_Livro_Temp, Ano_Publicacao_Livro_Temp, True)
            Lista_Livros_Auxiliar = Object_Biblioteca_Buscada_Atributo.Lista_Livros_Atributo
            Object_Biblioteca_Buscada_Atributo.Lista_Livros_Atributo = Lista_Livros_Auxiliar.append(Object_Livro_Temp)

        if Menu_Opcoes_Funcionario == 5 and Menu_Emprestar_Livro != 0:
            
            if Menu_Emprestar_Livro == 4:
                Menu_Emprestar_Livro = int(input("""
+------------------------------+
1- Buscar por titulo
2- Buscar por autor
0- Sair
+------------------------------+"""))
            
            if Menu_Emprestar_Livro == 1:
                Return_Function_Buscar_Function_O_F = Function_Buscar_Titulo_Global(Object_Biblioteca_Buscada_Atributo)
                Menu_Emprestar_Livro = Return_Function_Buscar_Function_O_F[2]              

            if Menu_Emprestar_Livro == 2:
                Return_Function_Buscar_Function_O_F = Function_Buscar_Autor_Global(Object_Biblioteca_Buscada_Atributo)
                Menu_Emprestar_Livro = Return_Function_Buscar_Function_O_F[2]
            
            if Menu_Emprestar_Livro == 3:
                del Object_Biblioteca_Buscada_Atributo.Lista_Livros_Atributo[Return_Function_Buscar_Function_O_F[2]]
                Menu_Emprestar_Livro = 4
            
            else:
                print("Numero invalido!!!")
                Menu_Emprestar_Livro = 4

        if Menu_Opcoes_Funcionario == 6 and Menu_Emprestar_Livro != 0:
            Menu_Alterar_Livro = 4
            Menu_Emprestar_Livro = 4
            if Menu_Emprestar_Livro == 4:
                Menu_Emprestar_Livro = int(input("""
+------------------------------+
1- Buscar por titulo
2- Buscar por autor
0- Sair
+------------------------------+"""))
            
            if Menu_Emprestar_Livro == 1:
                Return_Function_Buscar_Function_O_F = Function_Buscar_Titulo_Global(Object_Biblioteca_Buscada_Atributo)
                Menu_Emprestar_Livro = Return_Function_Buscar_Function_O_F[2]

            if Menu_Emprestar_Livro == 2:
               Return_Function_Buscar_Function_O_F = Function_Buscar_Autor_Global(Object_Biblioteca_Buscada_Atributo)
               Menu_Emprestar_Livro = Return_Function_Buscar_Function_O_F[2]

            if Menu_Emprestar_Livro == 3:
                if Menu_Alterar_Livro == 4:
                    Menu_Alterar_Livro = int(input("""
        +------------------------------+
        1- Alterar titulo
        2- Alterar autor
        3- Alterar ano de lancamento
        0- Sair
        +------------------------------+"""))
                
                if Menu_Alterar_Livro == 1:
                    Titulo_Livro_Temp = str(input("Digite o novo titulo do livro: "))  
                    Return_Function_Buscar_Function_O_F[0].Titulo_Atributo = Titulo_Livro_Temp       

                if Menu_Alterar_Livro == 2:
                    Autor_Livro_Temp = str(input("Digite o novo Autor do livro: "))  
                    Return_Function_Buscar_Function_O_F[0].Autor_Atributo = Autor_Livro_Temp
                
                if Menu_Alterar_Livro == 3:
                    Ano_Publicacao_Livro_Temp = str(input("Digite o novo titulo do livro: "))  
                    Return_Function_Buscar_Function_O_F[0].Ano_Publicacao_Atributo = Ano_Publicacao_Livro_Temp
                
                else:
                    print("Numero invalido!!!")
                    Menu_Alterar_Livro = 4

            else:
                print("Numero invalido!!!")
                Menu_Opcoes_Funcionario = 4

        else:
            print("Numero invalido!!!")
            Menu_Opcoes_Funcionario = 7
Menu_Login_SignUp = 5
Objects_Funcionarios = []
Livro = Class_Livro('Teste', 'teste', 2024)
Object_Biblioteca = Class_Biblioteca(Livro)
User_Criado = False
Funcionario_Criado = False

while Menu_Login_SignUp != 0:
    while Menu_Login_SignUp == 5:
        Menu_Login_SignUp = int(input("""
+------------------------------+
1- Login como Usuario
2- Login como Funcionario
3- Sign up Usuario
4- Sign up Funcionario
+------------------------------+
"""))
    
    while Menu_Login_SignUp == 1:
        if User_Criado: 
            Name_User_Buscado = str(input("Digite o nome do usuario: "))
            contador = 0
            Logged = False
            while contador < Object_Biblioteca.Lista_User_Atributos.__len__():
                if Object_Biblioteca.Lista_User_Atributos[contador].Nome_User_Atributo == Name_User_Buscado:
                    print("Login concluido!")
                    Object_User_Logged = Object_Biblioteca.Lista_User_Atributos[contador]
                    Logged = True
                    break
            if Logged == False:
                print("User não encontrado.")
            else:
                Function_Opcoes_User_And_Funcionario(Object_User_Logged ,Object_Biblioteca)

        else: 
            print("Nenhum Usuario Criado, Crie um usurio.")
            Menu_Login_SignUp = 3

    while Menu_Login_SignUp == 2:
        if Funcionario_Criado:
            Name_Funcionario_Buscado = str(input("Digite o nome do Funcionario: "))
            contador = 0
            Logged = False
            while contador < Objects_Funcionarios.__len__():
                if Objects_Funcionarios[contador].Nome_Funcionario_Atributo == Name_Funcionario_Buscado:
                    print("Login concluido!")
                    Object_Funcionario_Logged = Objects_Funcionarios[contador]
                    Logged = True
                    break
            if Logged == False:
                print("Funcionario não encontrado.")
            else:
                Function_Opcoes_Funcionarios(Object_Funcionario_Logged ,Object_Biblioteca)
            
        else: 
            print("Nenhum Funcionario Criado, Crie um Funcionario.")
            Menu_Login_SignUp = 4
    
    while Menu_Login_SignUp == 3:
        Nome_User_Temp = str(input("Digite o nome do usuario: "))
        Object_User_Logged = Class_User(Nome_User_Temp, None)
        Object_Biblioteca.Lista_User_Atributos.append(Object_User_Logged)
        Function_Opcoes_User_And_Funcionario(Object_User_Logged ,Object_Biblioteca)
        User_Criado = True
    
    while Menu_Login_SignUp == 4:
        Nome_Funcionario_Temp = str(input("Digite o nome do funcionario: "))
        Id_Funcionario_Temp = int(input("Digite o id do funcionario: "))
        Cargo_Funcionario_Temp = str(input("Digite o cargio do funcionario: "))
        Object_Funcionario_Logged = Class_Funcionario(Nome_Funcionario_Temp, Id_Funcionario_Temp, Cargo_Funcionario_Temp)
        Objects_Funcionarios.append(Object_Funcionario_Logged)
        Function_Opcoes_Funcionarios(Object_Funcionario_Logged ,Object_Biblioteca)
        Funcionario_Criado = True
