from abc import ABC, abstractmethod

### Para CRUD de aluno e professor ###

class Pessoa(ABC):
    def __init__(self, nome, cpf, rg, data_de_nascimento, nacionalidade, endereco, matricula):
        self.__nome = nome
        self.__cpf = cpf
        self.__rg = rg
        self.__data_de_nascimento = data_de_nascimento
        self.__nacionalidade = nacionalidade
        self.__matricula = matricula
        self.__endereco = endereco
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def rg(self):
        return self.__rg
    
    @property
    def data_de_nascimento(self):
        return self.__data_de_nascimento
    
    @property
    def nacionalidade(self):
        return self.__nacionalidade
    
    @property
    def endereco(self):
        return self.__endereco
    
    def alterar_endereco(self, novo_endereco):
        self.__endereco = novo_endereco
    # O endereço poderá ser alterado
    
    @property
    def matricula(self):
        return self.__matricula
    
class Aluno(Pessoa):
    def __init__(self, nome, cpf, rg, data_de_nascimento, nacionalidade, endereco, matricula):
        super().__init__(nome, cpf, rg, data_de_nascimento, nacionalidade, endereco, matricula)
        self.__indice = 0
    
    @property
    def indice(self):
        return self.__indice
    
    def alterar_indice(self, indice):
        self.__indice = indice
    # O índice, inicialmente zero, será alterado
    
class Professor(Pessoa):
    def __init__(self, nome, cpf, rg, data_de_nascimento, nacionalidade, endereco, matricula, formacao):
        super().__init__(nome, nome, cpf, rg, data_de_nascimento, nacionalidade, endereco, matricula)
        self.__formacao = formacao
        
    @property
    def formacao(self):
        return self.__formacao
    
    def atualizar_formacao(self, formacao):
        self.__formacao = formacao
        
 class Turma:
    def __init__(self, professor, id_turma, periodo_letivo, max_alunos, alunos=None):
        if not professor or not id_turma or not periodo_letivo or not max_alunos:
            raise ValueError("Todos os campos obrigatórios devem ser preenchidos.")
        self.professor = professor
        self.id_turma = id_turma
        self.alunos = alunos if alunos else []
        self.periodo_letivo = periodo_letivo
        self.max_alunos = max_alunos

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def remover_aluno(self, aluno):
        self.alunos.remove(aluno)
        
######################################
