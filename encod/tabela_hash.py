class Item:
    def __init__(self, valor):
        self.valor = valor

class Hash:
    def __init__(self, tamanho):
        self.qtd = 0
        self.tamanho = tamanho
        self.itens = [None for i in range(tamanho)]

    def __del__(self):
        return None

    def chave_div(self, chave):
        return (chave & 0x7FFFFFFF) % self.tamanho

    # def valor_string(self, chave):
    #     soma = 0
    #     inicio = 0
    #     final = len(chave)
    #     while inicio < final:
    #         valor = ord(chave[inicio]) + (7 * 31)
    #         soma = soma + valor
    #         inicio = inicio + 1
    #     indice = soma % self.tamanho
    #     return indice

    def valor_string(self, chave):
        valor = 7
        tam = len(chave)
        for i in range(tam):
            valor = valor * (7 + ord(chave[i]))
        return valor

    def sondagem_lin(self, pos, i):
        return ((pos + i) & 0x7FFFFFFF) % self.tamanho

    def insere(self, item):
        item = Item(item)
        if self.qtd == self.tamanho:
            raise IndexError("Tabela cheia!")
        chave = item.valor
        pos = self.valor_string(chave)
        for i in range(self.tamanho):
            new_pos = self.sondagem_lin(pos, i)
            if self.itens[new_pos] == None:
                self.itens[new_pos] = item
                self.qtd += 1
                return
    
    def busca(self, valor):
        chave = valor
        pos = self.valor_string(chave)
        for i in range(self.tamanho):
            new_pos = self.sondagem_lin(pos, i)
            if self.itens[new_pos]:
                if self.itens[new_pos].valor == valor:
                    return self.itens[new_pos]
        return None

    def mostrar_hash(self):
        for i in range(self.tamanho):
            print(self.itens[i].valor, end = " ")