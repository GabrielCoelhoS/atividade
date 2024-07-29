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
        
    def Function_Devolver_Livro_Class_User(self, Class_Livro_Atributo, Objeto_Livro_Devolvido_Atributo):
        i = 0
        while True:
            if self.Livros_Emprestados_User_Atributo[i] == Objeto_Livro_Devolvido_Atributo:
                Livros_Emprestados_User_Atributo_Auxiliar = self.Livros_Emprestados_User_Atributo
                Livros_Emprestados_User_Atributo_Auxiliar[i] = None
                Livros_Emprestados_User_Atributo_Auxiliar.sort()
                Class_Livro_Atributo.Function_Delvolver_Livro_Class_Livro()
                self.Livros_Emprestados_User_Atributo(Livros_Emprestados_User_Atributo_Auxiliar)
                break
            else:
                i += 1

    def Function_Exibir_Livros_Emprestados(self):
        for i in range(0, self.Livros_Emprestados_User_Atributo.len()):
            self.Livros_Emprestados_User_Atributo[i].Function_Exibir_Informacoes()

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
        
    def Function_Buscar_Titulo(self, Nome_Buscado):
        contador = 0
        while contador <= self.Lista_Livros_Atributos.len():
            if self.Lista_Livros_Atributos[contador] == Nome_Buscado:
                return self.Lista_Livros_Atributos[contador]
            else:
                print("Livro não encontrado!!")
            contador += 1
    
    encerrar = 1

    while encerrar != 0:
        while encerrar == 1:
            encerrar = int(input("""
+------------------------------+
 1- Entrar como Usuario
 2- Entrar como Funcionario
 3- Criar Usuario
+------------------------------+
"""))
