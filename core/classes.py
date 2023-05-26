from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, endereco, matricula, cpf, rg, data_de_nascimento, nacionalidade):
        self.__nome = nome
        self.__endereco = endereco
        self.__matricula = matricula
        self.__cpf = cpf
        self.__rg = rg
        self.__data_de_nascimento = data_de_nascimento
        self.__nacionalidade = nacionalidade
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
        
    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, novo_endereco):
        self.__endereco = novo_endereco
        
    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, novo_matricula):
        self.__matricula = novo_matricula
    
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
    
    
    
class Aluno(Pessoa):
    def __init__(self, nome, endereco, matricula, cpf, rg, data_de_nascimento, nacionalidade):
        super().__init__(nome, endereco, matricula, cpf, rg, data_de_nascimento, nacionalidade)
        self.__disciplinas_em_execucao = []
        self.__disciplinas_concluidas = []
        
    def iniciar_disciplina(self, codigo_disciplina):
        self.__disciplinas_em_execucao.append(codigo_disciplina)
        
    def terminar_disciplina(self, codigo_disciplina):
        self.__disciplinas_em_execucao.remove(codigo_disciplina)    
        self.__disciplinas_concluidas.append(codigo_disciplina)

    def verificar_disciplina(self, codigo_disciplina):
        if codigo_disciplina in self.__disciplinas_concluidas:
            return True
        else:
            return False
        
    def consultar_disciplinas_concluidas(self):
        disciplinas = []
        for codigo_disciplina in self.__disciplinas_concluidas:
            disciplinas.append(codigo_disciplina)
        return disciplinas
    
    def consultar_disciplinas_em_execucao(self):
        disciplinas = []
        for codigo_disciplina in self.__disciplinas_em_execucao:
            disciplinas.append(codigo_disciplina)
        return disciplinas
    
class Professor(Pessoa):
    def __init__(self, nome, endereco, matricula, cpf, rg, data_de_nascimento, nacionalidade, disciplinas_lecionadas, formacao):
        super().__init__(nome, endereco, matricula, cpf, rg, data_de_nascimento, nacionalidade)
        self.__formacao = formacao
        self.__disciplinas_leacionadas = []
        
    @property
    def formacao(self):
        return self.__formacao
    
    @formacao.setter
    def formacao(self, formacao):
        self.__formacao = formacao
        
    def iniciar_disciplina(self, codigo_disciplina):
        self.__disciplinas_leacionadas.append(codigo_disciplina)
        
    def terminar_disciplina(self, codigo_disciplina):
        self.__disciplinas_leacionadas.remove(codigo_disciplina)    

    def verificar_disciplina(self, codigo_disciplina):
        if codigo_disciplina in self.__disciplinas_leacionadas:
            return True
        else:
            return False
        
    def consultar_disciplinas_lecionadas(self):
        disciplinas = []
        for codigo_disciplina in self.__disciplinas_leacionadas:
            disciplinas.append(codigo_disciplina)
        return disciplinas
    
class Turma():
    def __init__(self, professor, codigo, numero_maximo_de_alunos):
        self.__professor = professor
        self.__codigo = codigo
        self.__numero_maximo_de_alunos = numero_maximo_de_alunos
        self.__quantidade_de_alunos = 0
        self.__alunos = []
        self.__periodo_letivo = []
        
    @property
    def professor(self):
        return self.__professor
    
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def numero_maximo_de_alunos(self):
        return self.__numero_maximo_de_alunos
    
    def inserir_aluno(self, aluno):
        if aluno not in self.__alunos and self.__quantidade_de_alunos + 1 < self.__numero_maximo_de_alunos:
            self.__alunos.append(aluno)
            self.__quantidade_de_alunos += 1
            return True
        else:
            return False
        
    def verificar_aluno(self, aluno):
        if aluno in self.__alunos:
            return True
        else:
            return False
        
    def remover_aluno(self, aluno):
        if aluno in self.__alunos:
            self.__alunos.remove(aluno)
            self.__quantidade_de_alunos -= 1
            return True
        else:
            return False
        
    def definir_periodo_letivo(self, inicio, fim):
        self.__periodo_letivo[0] = inicio
        self.__periodo_letivo[1] = fim
        