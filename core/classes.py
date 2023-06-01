from abc import ABC, abstractmethod

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
    
    @endereco.setter
    def endereco(self, novo_endereco):
        self.__endereco = novo_endereco
    # O endereço pode ser alterado no futuro
    
    @property
    def matricula(self):
        return self.__matricula
    
class Aluno(Pessoa):
    def __init__(self, nome, cpf, rg, data_de_nascimento, nacionalidade, endereco, matricula, indice):
        super().__init__(nome, nome, cpf, rg, data_de_nascimento, nacionalidade, endereco, matricula)
        self.__indice = indice
    
    @property
    def indice(self):
        return self.__indice
    
    @indice.setter
    def indice(self, indice):
        self.__indice = indice
    
class Professor(Pessoa):
    def __init__(self, nome, cpf, rg, data_de_nascimento, nacionalidade, endereco, matricula, formacao):
        super().__init__(nome, nome, cpf, rg, data_de_nascimento, nacionalidade, endereco, matricula)
        self.__formacao = formacao
        
    @property
    def formacao(self):
        return self.__formacao
    
    @formacao.setter
    def formacao(self, formacao):
        self.__formacao = formacao