class No:
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None
        self.qtd_nos = 0

    def inicializar(self):
        self.raiz = No(0)
        for i in range(16):
            valor = bin(i)
            valor = valor.replace("0b", "")
            if len(valor) < 4:
                s = ""
                for j in range(4-len(valor)):
                    s += "0"
                valor = s + valor
            
            ant = None
            atual = self.raiz
            for v in valor:
                ant = atual
                if v == "0":
                    if ant.esq:
                        atual = atual.esq
                    else:
                        atual = No(int(v))
                        ant.esq = atual
                elif v == "1":
                    if ant.dir:
                        atual = atual.dir
                    else:
                        atual = No(int(v))
                        ant.dir = atual

    def __del__(self):
        return

    def vazia(self, node = None):
        if node is None:
            node = self.raiz
        if node:
            return False
        return True

    def altura(self, node):
        if not node:
            return 0
        if self.vazia(node):
            return 0
        alt_esq = self.altura(node.esq)
        alt_dir = self.altura(node.dir)
        if alt_esq > alt_dir:
            return (alt_esq + 1)
        else:
            return (alt_dir + 1)
    
    def pre_ordem(self, node = None):
        if not node:
            return
        s = str(node.dado)
        s += str(self.pre_ordem(node.esq))
        s += str(self.pre_ordem(node.dir))
        s = s.replace("None", "")
        return s

    def em_ordem(self, node = None):
        if not node:
            return
        s = ""
        s += str(self.em_ordem(node.esq))
        s += str(node.dado)
        s += str(self.em_ordem(node.dir))
        s = s.replace("None", "")
        return s

    def pos_ordem(self, node = None):
        if not node:
            return
        s = ""
        s += str(self.pos_ordem(node.esq))
        s += str(self.pos_ordem(node.dir))
        s += str(node.dado)
        s = s.replace("None", "")
        return s

    def construtor(self, string):
        numbers = []
        for i in range(32):
            valor = bin(i)
            valor = valor.replace("0b", "")
            if len(valor) < 5:
                s = ""
                for j in range(5-len(valor)):
                    s += "0"
                valor = s + valor
            numbers.append(valor)

        string = string.replace("0", "")
        string = string.replace("1", "")
        for i in range(len(string)):
            self.insere(string[i], numbers[i])                
        
            
    def insere(self, valor, pos):
        novo = No(valor)
        ant = None
        atual = self.raiz
        for p in pos:
            ant = atual
            if p == "0":
                if ant.esq:
                    atual = atual.esq
                else:
                    atual = novo
                    ant.esq = atual
            elif p == "1":
                if ant.dir:
                    atual = atual.dir
                else:
                    atual = novo
                    ant.dir = atual
        return novo.dado
    
    def consultar(self, valor):
        ant = None
        atual = self.raiz
        for v in valor:
            ant = atual
            if v == "0":
                if ant.esq:
                    atual = atual.esq
            elif v == "1":
                if ant.dir:
                    atual = atual.dir
        return atual.dado


# arvore = ArvoreBinaria()

# arvore.inicializar()

# r = arvore.pre_ordem(arvore.raiz)
# print(r)
# r = arvore.em_ordem(arvore.raiz)
# print(r)
# r = arvore.pos_ordem(arvore.raiz)
# print(r)
