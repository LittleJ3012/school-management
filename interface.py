'''
    Interface de Gerenciamento de Alunos
    Rafael Renó Corrêa, 31/05/2023
    v.1.0
'''

import tkinter as tk
import core.classes as tipo
from tkinter import messagebox

class EstruturaAlunos():
    def __init__(self):
        self.__lista_alunos = []

class CaixaVazia(Exception):
    pass

class GerenciarAluno(tk.Tk): # Onde ocorre o cadastro!
    def __init__(self, lista_alunos):
        super().__init__()
        
        ### Estruturas de Dados ###
        self.__lista_alunos = lista_alunos
        self.indice = 0
        ###########################
        
        #self.janela = tk.Tk()
        self.title('Gerenciar Aluno')
        self.geometry('1280x720')

        self.frameBase = tk.Frame(self)
        self.frameTopo = tk.Frame(self)
        
        ### Entrada de Dados ###
        self.labelNome = tk.Label(self.frameTopo, text = 'Nome:')
        self.inputNome = tk.Entry(self.frameTopo, width = 20)
        self.labelNome.pack()
        self.inputNome.pack()
        self.labelCPF = tk.Label(self.frameTopo, text = 'CPF:')
        self.inputCPF = tk.Entry(self.frameTopo, width = 20)
        self.labelCPF.pack()
        self.inputCPF.pack()
        self.labelRG = tk.Label(self.frameTopo, text = 'RG:')
        self.inputRG = tk.Entry(self.frameTopo, width = 20)
        self.labelRG.pack()
        self.inputRG.pack()
        self.labelData_de_nascimento = tk.Label(self.frameTopo, text = 'Data de nascimento:')
        self.inputData_de_nascimento = tk.Entry(self.frameTopo, width = 20)
        self.labelData_de_nascimento.pack()
        self.inputData_de_nascimento.pack()
        self.labelNacionalidade = tk.Label(self.frameTopo, text = 'Nacionalidade:')
        self.inputNacionalidade = tk.Entry(self.frameTopo, width = 20)
        self.labelNacionalidade.pack()
        self.inputNacionalidade.pack()
        self.labelMatricula = tk.Label(self.frameTopo, text = 'Matricula:')
        self.inputMatricula = tk.Entry(self.frameTopo, width = 20)
        self.labelMatricula.pack()
        self.inputMatricula.pack()
        self.labelEndereco = tk.Label(self.frameTopo, text = 'Endereço:')
        self.inputEndereco = tk.Entry(self.frameTopo, width = 20)
        self.labelEndereco.pack()
        self.inputEndereco.pack()  
        ########################
        
        self.aluno = tipo.Aluno(self.inputNome, self.inputCPF, self.inputRG, self.inputData_de_nascimento, self.inputNacionalidade, self.inputMatricula, self.inputEndereco, self.indice)
        
        ### Botões de Confirmação ###
        self.botaoCadastrar = tk.Button(self.frameBase, text = 'Cadastrar', command = lambda: self.cadastrar_aluno(self.__lista_alunos, self.aluno))
        self.botaoExcluir = tk.Button(self.frameBase, text = 'Excluir', command = self.excluir_aluno)
        self.botaoEditar = tk.Button(self.frameBase, text = 'Editar')
        
        self.botaoCadastrar.pack(side = 'left')
        self.botaoEditar.pack(side = 'left')
        self.botaoExcluir.pack(side = 'right')
        #############################
        
        self.frameBase.pack(side = 'bottom')
        self.frameTopo.pack(side = 'top')
        
        self.mainloop()
        
    def cadastrar_aluno(self, lista_alunos, aluno):
        # log
        print("Botão 'Cadastrar' em 'Gerenciar Aluno' pressionado.")
        #
        lista_alunos.append(aluno)
        messagebox.showinfo('Sucesso!', 'Aluno cadastrado com sucesso!')

    def excluir_aluno(self):
        # log
        print("Botão 'Excluir' em 'Gerenciar Aluno' pressionado.")
        #
        janela_exclusao = ExcluirAluno(self, self.__lista_alunos)
        janela_exclusao.mainloop()
        
class ExcluirAluno(tk.Toplevel):
    def __init__(self, GerenciarAluno, lista_alunos):
        super().__init__(GerenciarAluno)
        self.title('Remover Aluno')
        self.geometry('400x300')
        self.__lista_alunos = lista_alunos
        
        self.frameBase = tk.Frame(self)
        self.frameTopo = tk.Frame(self)
        
        ### Entrada de Dados ###
        self.labelMatricula = tk.Label(self.frameTopo, text = 'Matricula:')
        self.inputMatricula = tk.Entry(self.frameTopo, width = 20)
        self.labelMatricula.pack()
        self.inputMatricula.pack()
        ########################
        
        ### Botão de Confirmação ###
        self.botaoExcluir = tk.Button(self.frameBase, text = 'Confirmar', command = lambda: self.confirmar_exclusao(self.__lista_alunos, self.inputMatricula))
        self.botaoExcluir.pack()
        
        self.frameBase.pack(side = 'bottom')
        self.frameTopo.pack(side = 'top')
        ############################
        
    def confirmar_exclusao(self, lista_alunos, matricula):
        # log
        print("Botão 'Confimar' em 'Remover Aluno' pressionado.")
        #
        for aluno in lista_alunos:
            if aluno.matricula == matricula:
                self.remove(aluno)
                messagebox.showinfo('Sucesso!', 'Aluno removido do banco de dados!')
            else:
                messagebox.showerror('Erro!', 'Aluno não encontrado.')
           
           
                
def main():
    lista_alunos = EstruturaAlunos()
    GerenciarAluno(lista_alunos)
    
main()