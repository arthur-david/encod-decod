from no import No

class BST:
    def __init__(self):
        self._raiz = None
        self._nos = 0
        
    def inserir(self, valor):
        no = No(valor)
        if self._raiz == None:
            self._raiz = no
            self._nos = self._nos + 1
        else:
            atual = self._raiz
            pai = None
            while True:
                if atual != None:
                    pai = atual
                    if no.valor < atual.valor:
                        atual = atual.esquerda
                    else:
                        atual = atual.direita
                else:
                    if no.valor < pai.valor:
                        pai.esquerda = no
                        self._nos = self._nos + 1
                        return
                    else:
                        pai.direita = no
                        self._nos = self._nos + 1
                        return

    def remover(self, valor):
        if self._raiz == None:
            raise Exception('A arvore esta vazia.')
        atual = self._raiz
        while atual != None:
            if valor == atual.valor:
                if atual == self._raiz:
                    self._raiz = self._auxiliarRemocao(atual)
                    self._nos = self._nos - 1
                else:
                    if anterior.direita == atual:
                        anterior.direita = self._auxiliarRemocao(atual)
                        self._nos = self._nos - 1
                    else:
                        anterior.esquerda = self._auxiliarRemocao(atual)
                        self._nos = self._nos - 1
            anterior = atual
            if valor > atual.valor:
                atual = atual.direita
            else:
                atual = atual.esquerda
    
    def _auxiliarRemocao(self, atual):
        if atual.esquerda == None:
            no_2 = atual.direita
            return no_2
        no_1 = atual
        no_2 = atual.esquerda
        while no_2.direita != None:
            no_1 = no_2
            no_2 = no_2.direita
        if no_1 != atual:
            no_1.direita = no_2.esquerda
            no_2.esquerda = atual.esquerda
        no_2.direita = atual.direita
        return no_2

    def busca(self, valor):
        if self._raiz == None:
            raise Exception('A arvore esta vazia.')

        atual = self._raiz
        while atual != None:
            if valor == atual.valor:
                return True
            if valor > atual.valor:
                atual = atual.direita
            else:
                atual = atual.esquerda
        return False

    def preOrdem(self, no):
        if self._raiz == None:
            raise Exception('A arvore esta vazia.')
        if no != None:
            print(no.valor)
            self.preOrdem(no.esquerda)
            self.preOrdem(no.direita)
    
    def Ordem(self, no):
        if self._raiz == None:
            raise Exception('A arvore esta vazia.')
        if no != None:
            self.Ordem(no.esquerda)
            print(no.valor)
            self.Ordem(no.direita)

    def posOrdem(self, no):
        if self._raiz == None:
            raise Exception('A arvore esta vazia.')
        if no != None:
            self.posOrdem(no.esquerda)
            self.posOrdem(no.direita)
            print(no.valor)

    def restauraABB(self):
        self._raiz = None
        self._nos = 0

    def obterRaiz(self):
        return self._raiz

    def quantidadeNos(self):
        return self._nos

    def altura(self, no):
        if no == None:
            return 0
        else:
            altura_esq = self.altura(no.esquerda)
            altura_dir = self.altura(no.direita)
            if altura_esq > altura_dir:
                return altura_esq + 1
            return altura_dir + 1
    
    def arvoresIguais(self, a1_r, a2_r):
        """São passados as raizes das arvores para a funcao"""
        if a1_r == None and a2_r == None:
            return True
        elif a1_r != None and a2_r != None:
            return ((a1_r.valor == a2_r.valor) and self.arvoresIguais(a1_r.esquerda, a2_r.esquerda) and self.arvoresIguais(a1_r.direita, a2_r.direita))
        return False

    def __del__(self):
        return


insercao = [25, 10, 8, 3, 1, 15, 75, 17, 30, 28, 27, 52, 70, 65, 73]
bst = BST()
for i in range(len(insercao)):
    bst.inserir(insercao[i])

raiz = bst.obterRaiz()

remocao = [28, 15, 75, 1]
for r in range(len(remocao)):
    bst.remover(remocao[r])

print()
raiz = bst.obterRaiz()
bst.posOrdem(raiz)

