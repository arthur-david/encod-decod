class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
    
    def filhoEsquerda(self):
        return self.esquerda
    
    def filhoDireita(self):
        return self.direita
    