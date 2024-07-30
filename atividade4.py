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
        for i in range(0, self.Livros_Emprestados_User_Atributo.len()):
            self.Livros_Emprestados_User_Atributo[i].Function_Exibir_Informacoes()
    
    def Function_Buscar_Titulo_Livro_Emprestado(self, Titulo_Buscado):
        contador = 0
        while contador <= self.Livros_Emprestados_User_Atributo.len():
            if self.Livros_Emprestados_User_Atributo[contador].Titulo_Atributo == Titulo_Buscado:
                return self.Livros_Emprestados_User_Atributo[contador] #Pode não parar o while
            else:
                contador += 1
    
    def Function_Buscar_Autor_Livro_Emprestado(self, Autor_Buscado):
        contador = 0
        while contador <= self.Livros_Emprestados_User_Atributo.len():
            if self.Livros_Emprestados_User_Atributo[contador].Autor_Atributo == Autor_Buscado:
                print("Livro encontrado!!")
                return self.Livros_Emprestados_User_Atributo[contador]
            else:
                print("Livro não encontrado!!")
            contador += 1

class Class_Funcionario(Class_User):
    def __init__(self, Nome_Fucionario_Atributo, Livros_Emprestados_Fucionario_Atributo, ID_Funcionario_Atributo, Cargo_Funcionario_Atributo):
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
    def __init__(self, Lista_Livros_Atributo, Lista_User_Atributo):
        self.Lista_Livros_Atributos = Lista_Livros_Atributo
        self.Lista_User_Atributos = Lista_User_Atributo

    def Function_Add_User(self, Nome_User_Atributo, Livros_Emprestados_User_Atributo):
        Object_User_Temp = Class_User(Nome_User_Atributo, Livros_Emprestados_User_Atributo)
        self.Lista_User_Atributo.append(Object_User_Temp)
    
    def Function_Remove_User(self, Posicao_User_Atributo):
        del self.Lista_User_Atributo[Posicao_User_Atributo]
        
    def Function_Buscar_Titulo(self, Titulo_Buscado):
        contador = 0
        while contador <= self.Lista_Livros_Atributos.len():
            if self.Lista_Livros_Atributos[contador].Titulo_Atributo == Titulo_Buscado:
                return self.Lista_Livros_Atributos[contador]
            else:
                print("Livro não encontrado!!")
            contador += 1
    def Function_Buscar_Autor(self, Autor_Buscado):
        contador = 0
        while contador <= self.Lista_Livros_Atributos.len():
            if self.Lista_Livros_Atributos[contador].Autor_Atributo == Autor_Buscado:
                print("Livro encontrado!!")
                return self.Lista_Livros_Atributos[contador]
            else:
                print("Livro não encontrado!!")
            contador += 1
    
def Function_Exibir_Livro(Object_livro_Exibir):
    print(f"""|   Titulo   |   Autor   |   Ano de Publicacao   |   Disponibilidade   |
|   {Object_livro_Exibir.Titulo_Atributo}   |   {Object_livro_Exibir.Autor_Atributo}   |   {Object_livro_Exibir.Ano_Publicacao_Atributo}   |   {Object_livro_Exibir.Disponibilidade_Atributo}   |""")

def Function_Opcoes_User(Object_User_Atributo, Object_Biblioteca_Buscada_Atributo):
    Menu_Opcoes_User = 5
    while Menu_Opcoes_User != 0:
        while Menu_Opcoes_User == 5:
            Menu_Emprestar_Livro = 4
            Menu_Opcoes_User = int(input("""
+------------------------------+
 1-Pegar livro emprestado
 2-Devolver Livro
 3-Ver livros pegos
 0-Sair
+------------------------------+
"""))
        while Menu_Opcoes_User == 1 and Menu_Emprestar_Livro != 0:
            while Menu_Emprestar_Livro == 4:
                Menu_Emprestar_Livro = int(input("""
+------------------------------+
1- Buscar por titulo
2- Buscar por autor
0- Sair
+------------------------------+"""))
            while Menu_Emprestar_Livro == 1:
                Titulo_Buscado = str(input("Digite o titulo do livro: "))
                Object_Livro_Buscado = Object_biblioteca_Buscada_Atributo.Function_Buscar_Titulo(Titulo_Buscado)
                Function_Exibir_Livro(Object_Livro_Buscado)
                Menu_Emprestar_Livro = int(input("""
+------------------------------+
1- Buscar outro
3- Pegar emprestado
4- Voltar
+------------------------------+"""))

            while Menu_Emprestar_Livro == 2:
                Autor_Buscado = str(input("Digite o autor do livro: "))
                Object_Livro_Buscado = Object_biblioteca_Buscada_Atributo.Function_Buscar_Autor(Titulo_Buscado)
                Function_Exibir_Livro(Object_Livro_Buscado)
                Menu_Emprestar_Livro = int(input("""
+------------------------------+
2- Buscar outro
3- Pegar emprestado
4- Voltar
+------------------------------+"""))
            
            while Menu_Emprestar_Livro == 3:

                Emprestado = Object_User_Atributo.Function_Emprestar_Livros_Class_User(Object_Livro_Buscado)
                if Emprestado:
                    print("Livro emprestado com sucesso!")
                else:
                    print("Livro indisponivel")
                Menu_Emprestar_Livro = 4
        
        while Menu_Opcoes_User == 2 and Menu_Emprestar_Livro != 0:
            
            while Menu_Emprestar_Livro == 3:
                Menu_Emprestar_Livro = int(input("""
+------------------------------+
1- Buscar por titulo
2- Buscar por autor
0- Sair
+------------------------------+"""))
            while Menu_Emprestar_Livro == 1:
                Titulo_Buscado = str(input("Digite o titulo do livro: "))
                Object_Livro_Buscado = Object_biblioteca_Buscada_Atributo.Function_Buscar_Titulo_Livro_Emprestado(Titulo_Buscado)
                Function_Exibir_Livro(Object_Livro_Buscado)
                Menu_Emprestar_Livro = int(input("""
+------------------------------+
1- Buscar outro
3- Voltar
4- Pegar emprestado
+------------------------------+"""))

            while Menu_Emprestar_Livro == 2:
                Autor_Buscado = str(input("Digite o autor do livro: "))
                Object_Livro_Buscado = Object_biblioteca_Buscada_Atributo.Function_Buscar_Autor_Livro_Emprestado(Autor_Buscado)
                Function_Exibir_Livro(Object_Livro_Buscado)
                Menu_Emprestar_Livro = int(input("""
+------------------------------+
2- Buscar outro
3- Voltar
4- Pegar emprestado
+------------------------------+"""))    
        
        while Menu_Opcoes_User == 3:
            for i in range(0, Object_User_Atributo.Livros_Emprestados_User_Atributo.len()):
                Function_Exibir_Livro(Object_User_Atributo.Livros_Emprestados_User_Atributo[i])

def Function_Opcoes_Funcionarios(Object_Funcionario_Atributo, Object_Biblioteca_Buscada_Atributo):
    Menu_Opcoes_Funcionario = 5
    while Menu_Opcoes_Funcionario != 0:
        while Menu_Opcoes_Funcionario == 5:
            Menu_Emprestar_Livro = 4
            Menu_Opcoes_Funcionario = int(input("""
+------------------------------+
 1-Pegar livro emprestado
 2-Devolver Livro
 3-Ver livros pegos
 0-Sair
+------------------------------+
"""))
        while Menu_Opcoes_Funcionario == 1 and Menu_Emprestar_Livro != 0:
            while Menu_Emprestar_Livro == 4:
                Menu_Emprestar_Livro = int(input("""
+------------------------------+
1- Buscar por titulo
2- Buscar por autor
0- Sair
+------------------------------+"""))
            while Menu_Emprestar_Livro == 1:
                Titulo_Buscado = str(input("Digite o titulo do livro: "))
                Object_Livro_Buscado = Object_biblioteca_Buscada_Atributo.Function_Buscar_Titulo(Titulo_Buscado)
                Function_Exibir_Livro(Object_Livro_Buscado)
                Menu_Emprestar_Livro = int(input("""
+------------------------------+
1- Buscar outro
3- Pegar emprestado
4- Voltar
+------------------------------+"""))

            while Menu_Emprestar_Livro == 2:
                Autor_Buscado = str(input("Digite o autor do livro: "))
                Object_Livro_Buscado = Object_biblioteca_Buscada_Atributo.Function_Buscar_Autor(Titulo_Buscado)
                Function_Exibir_Livro(Object_Livro_Buscado)
                Menu_Emprestar_Livro = int(input("""
+------------------------------+
2- Buscar outro
3- Pegar emprestado
4- Voltar
+------------------------------+"""))
            
            while Menu_Emprestar_Livro == 3:

                Emprestado = Object_User_Atributo.Function_Emprestar_Livros_Class_User(Object_Livro_Buscado)
                if Emprestado:
                    print("Livro emprestado com sucesso!")
                else:
                    print("Livro indisponivel")
                Menu_Emprestar_Livro = 4
        
        while Menu_Opcoes_Funcionario == 2 and Menu_Emprestar_Livro != 0:
            
            while Menu_Emprestar_Livro == 3:
                Menu_Emprestar_Livro = int(input("""
+------------------------------+
1- Buscar por titulo
2- Buscar por autor
0- Sair
+------------------------------+"""))
            while Menu_Emprestar_Livro == 1:
                Titulo_Buscado = str(input("Digite o titulo do livro: "))
                Object_Livro_Buscado = Object_biblioteca_Buscada_Atributo.Function_Buscar_Titulo_Livro_Emprestado(Titulo_Buscado)
                Function_Exibir_Livro(Object_Livro_Buscado)
                Menu_Emprestar_Livro = int(input("""
+------------------------------+
1- Buscar outro
3- Voltar
4- Pegar emprestado
+------------------------------+"""))

            while Menu_Emprestar_Livro == 2:
                Autor_Buscado = str(input("Digite o autor do livro: "))
                Object_Livro_Buscado = Object_biblioteca_Buscada_Atributo.Function_Buscar_Autor_Livro_Emprestado(Autor_Buscado)
                Function_Exibir_Livro(Object_Livro_Buscado)
                Menu_Emprestar_Livro = int(input("""
+------------------------------+
2- Buscar outro
3- Voltar
4- Pegar emprestado
+------------------------------+"""))    
        
        while Menu_Opcoes_Funcionario == 3:

Menu_Login_SignUp = 5
Objects_Users = []
Object_Biblioteca = None

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
        Name_User_Buscado = str(input("Digite o nome do usuario: "))
        contador = 0
        Logged = False
        while contador < Objects_Users.len():
            if Objects_Users[contador].Nome_User_Atributo == Name_User_Buscado:
                print("Login concluido!")
                Object_User_Logged = Objects_Users[contador]
                Logged = True
                break
        if Logged == False:
            print("User não encontrado.")
        else:
            Function_Opcoes_User(Object_User_Logged ,Object_Biblioteca)

            
                
            

