'''
    Interface de Gerenciamento de Alunos
    Rafael Renó Corrêa, 31/05/2023
    v.1.0
'''

import tkinter as tk
import core.classes as tipo
from tkinter import messagebox

class Gerenciar(tk.Tk): # Onde ocorre o cadastro!
    def __init__(self, struct_alunos):
        super().__init__()
        
        ### Estruturas de Dados ###       
        self.__alunos = struct_alunos
        ###########################
        
        self.title('Gerenciar Aluno')
        self.geometry('800x600')

        self.frameTopo = tk.Frame(self)
        self.frameMeio = tk.Frame(self)
        self.frameBase = tk.Frame(self)
        
        ### Entrada de Dados ###
        
        # Nome #
        self.frameNome = tk.Frame(self.frameMeio)
        self.labelNome = tk.Label(self.frameNome, text = 'Nome:')
        self.inputNome = tk.Entry(self.frameNome, width = 20)
        self.labelNome.pack(side = 'left')
        self.inputNome.pack(side = 'right')
        self.frameNome.pack()
        ########
        
        # CPF #
        self.frameCPF = tk.Frame(self.frameMeio)
        self.labelCPF = tk.Label(self.frameCPF, text = 'CPF:')
        self.inputCPF = tk.Entry(self.frameCPF, width = 20)
        self.labelCPF.pack(side = 'left')
        self.inputCPF.pack(side = 'right')
        self.frameCPF.pack()
        #######
        
        # RG #
        self.frameRG = tk.Frame(self.frameMeio)
        self.labelRG = tk.Label(self.frameRG, text = 'RG:')
        self.inputRG = tk.Entry(self.frameRG, width = 20)
        self.labelRG.pack(side = 'left')
        self.inputRG.pack(side = 'right')
        self.frameRG.pack()
        ######
        
        # Data de nascimento #
        self.frameData_de_nascimento = tk.Frame(self.frameMeio)
        self.labelData_de_nascimento = tk.Label(self.frameData_de_nascimento, text = 'Data de nascimento:')
        self.inputData_de_nascimento = tk.Entry(self.frameData_de_nascimento, width = 20)
        self.labelData_de_nascimento.pack(side = 'left')
        self.inputData_de_nascimento.pack(side = 'right')
        self.frameData_de_nascimento.pack()
        ######################
        
        # Nacionalidade #
        self.frameNacionalidade = tk.Frame(self.frameMeio)
        self.labelNacionalidade = tk.Label(self.frameNacionalidade, text = 'Nacionalidade:')
        self.inputNacionalidade = tk.Entry(self.frameNacionalidade, width = 20)
        self.labelNacionalidade.pack(side = 'left')
        self.inputNacionalidade.pack(side = 'right')
        self.frameNacionalidade.pack()
        #################
        
        # Endereço #
        self.frameEndereco = tk.Frame(self.frameMeio)
        self.labelEndereco = tk.Label(self.frameEndereco, text = 'Endereço:')
        self.inputEndereco = tk.Entry(self.frameEndereco, width = 20)
        self.labelEndereco.pack(side = 'left')
        self.inputEndereco.pack(side = 'right')
        self.frameEndereco.pack()
        ############
        
        # Matricula #
        self.frameMatricula = tk.Frame(self.frameMeio)
        self.labelMatricula = tk.Label(self.frameMatricula, text = 'Matricula:')
        self.inputMatricula = tk.Entry(self.frameMatricula, width = 20)
        self.labelMatricula.pack(side = 'left')
        self.inputMatricula.pack(side = 'right')
        self.frameMatricula.pack()
        #############
        
        ########################
        
        ### Botões de Confirmação ###
        self.botaoCadastrar = tk.Button(self.frameBase, text = 'Cadastrar', command = self.CadastrarAluno)
        self.botaoExcluir = tk.Button(self.frameBase, text = 'Excluir', command = self.ExcluirAluno)
        self.botaoEditar = tk.Button(self.frameBase, text = 'Editar', command = self.EditarAluno)
        
        self.botaoCadastrar.pack(side = 'left')
        self.botaoEditar.pack(side = 'left')
        self.botaoExcluir.pack(side = 'right')
        #############################
        
        self.labelTopo = tk.Label(self.frameTopo, text = 'Cadastrar Aluno:')
        
        self.frameTopo.pack(side = 'top')
        self.frameMeio.pack()
        self.frameBase.pack(side = 'bottom')
        
        self.mainloop()
        
    def CadastrarAluno(self):
        # log
        print("Botão 'Cadastrar' em 'Gerenciar Aluno' pressionado.")
        #
        nome = self.inputNome.get()
        cpf = self.inputCPF.get()
        rg = self.inputRG.get()
        data_de_nascimento = self.inputData_de_nascimento.get()
        nacionalidade = self.inputNacionalidade.get()
        endereco = self.inputEndereco.get()
        matricula = self.inputMatricula.get()
        
        aluno = tipo.Aluno(nome, cpf, rg, data_de_nascimento, nacionalidade, endereco, matricula)
        self.__alunos.append(aluno)
        messagebox.showinfo('Sucesso!', 'Aluno cadastrado com sucesso!\nNome: {}\nCPF: {}\nRG: {}\nData de nascimento: {}\nMatrícula: {}\nEndereço: {}\nÍndice: {}'.format(aluno.nome, aluno.cpf, aluno.rg, aluno.data_de_nascimento, aluno.matricula, aluno.endereco, aluno.indice))

    def ExcluirAluno(self):
        # log
        print("Botão 'Excluir' em 'Gerenciar Aluno' pressionado.")
        #
        janela_exclusao = Excluir(self, self.__alunos)
        janela_exclusao.mainloop()
        
    def EditarAluno(self):
        # log
        print("Botão 'Editar' em 'Gerenciar Aluno' pressionado.")
        #
        janela_edicao = Editar(self, self.__alunos)
        janela_edicao.mainloop()
        
class Excluir(tk.Toplevel):
    def __init__(self, Gerenciar, alunos): # Erro ao receber "alunos" como parâmetro!
        super().__init__(Gerenciar)
        self.title('Excluir Aluno')
        self.geometry('400x300')
        self.__alunos = alunos
        
        self.frameMeio = tk.Frame(self)
        self.frameBase = tk.Frame(self)
        
        ### Entrada de Dados ###
        self.labelMatricula = tk.Label(self.frameMeio, text = 'Matricula:')
        self.inputMatricula = tk.Entry(self.frameMeio, width = 20)
        self.labelMatricula.pack()
        self.inputMatricula.pack()
        ########################
        
        self.frameMeio.pack()
        
        ### Botão de Confirmação ###
        self.botaoExcluir = tk.Button(self.frameBase, text = 'Confirmar', command = self.ConfirmarExclusao)
        self.botaoExcluir.pack()
        ############################
        
        self.frameBase.pack(side = 'bottom')
        
    def ConfirmarExclusao(self): # "self" é a janela de exclusão
        # log #
        print("Botão 'Confirmar' em 'Remover Aluno' pressionado.")
        #######
        
        matricula = self.inputMatricula.get()
        
        flag = False
        
        print(matricula) # Por que não carrega informação?
        
        for aluno in self.__alunos:
            if aluno.matricula == matricula:
                flag = True
        if flag == True:
            self.__alunos.remove(aluno)
            messagebox.showinfo('Sucesso!', 'Aluno removido do banco de dados!')
            self.destroy()
        else:
            messagebox.showerror('Erro!', 'Aluno não encontrado.')
            
class Editar(tk.Toplevel):
    def __init__(self, Gerenciar, alunos): # Erro ao receber "alunos" como parâmetro!
        super().__init__(Gerenciar)
        self.title('Editar Aluno')
        self.geometry('400x300')
        self.__alunos = alunos
        
        self.frameMeio = tk.Frame(self)
        self.frameBase = tk.Frame(self)
        
        ### Entrada de Dados ###
        
        # Matrícula #
        self.frameMatricula = tk.Frame(self.frameMeio)
        self.labelMatricula = tk.Label(self.frameMatricula, text = 'Matricula:')
        self.inputMatricula = tk.Entry(self.frameMatricula, width = 20)
        self.labelMatricula.pack(side = 'left')
        self.inputMatricula.pack(side = 'right')
        self.frameMatricula.pack()
        #############
        
        # Endereço #
        self.frameEndereco = tk.Frame(self.frameMeio)
        self.labelEndereco = tk.Label(self.frameEndereco, text = 'Novo endereço:')
        self.inputEndereco = tk.Entry(self.frameEndereco, width = 20)
        self.labelEndereco.pack(side = 'left')
        self.inputEndereco.pack(side = 'right')
        self.frameEndereco.pack()
        ############
        
        ########################
        
        self.frameMeio.pack()
        
        ### Botão de Confirmação ###
        self.botaoEditar = tk.Button(self.frameBase, text = 'Confirmar', command = self.ConfirmarEdicao)
        self.botaoEditar.pack()
        ############################
        
        self.frameBase.pack(side = 'bottom')
        
    def ConfirmarEdicao(self): # "self" é a janela de exclusão
        # log #
        print("Botão 'Confirmar' em 'Editar Aluno' pressionado.")
        #######
        
        matricula = self.inputMatricula.get()
        endereco = self.inputEndereco.get()
        
        flag = False
        
        print(matricula) # Por que não carrega informação?
        
        for aluno in self.__alunos:
            if aluno.matricula == matricula:
                aluno.alterar_endereco(endereco)
                flag = True
        if flag == True:
            messagebox.showinfo('Sucesso!', 'Aluno alterado no banco de dados!')
            self.destroy()
        else:
            messagebox.showerror('Erro!', 'Aluno não encontrado.')