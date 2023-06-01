import tkinter as tk
import core.classes as tipo

class GUI():
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title('Aluno')
        self.janela.geometry('400x300')
        
        # Botões de confirmação
        self.frameBase = tk.Frame(self.janela)
        self.labelCadastrar = tk.Label(self.frameBase, text = 'Cadastrar')
        self.labelExcluir = tk.Label(self.frameBase, text = 'Cadastrar')
        self.labelEditar = tk.Label(self.frameBase, text = 'Cadastrar')
        
        self.labelCadastrar.pack()
        self.labelEditar.pack()
        self.labelExcluir.pack()
        
        self.frameBase.pack(side = 'bottom')
        
        self.janela.mainloop()
        
def main():
    GUI()
    
main()