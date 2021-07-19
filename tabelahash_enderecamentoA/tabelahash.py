from itemhash import ItemHash

class TabelaHash:
    def __init__(self, tamanho=101):
        self._tamanho = tamanho
        self._tabela = [None] * self._tamanho
        self._quantidade_elementos = 0
        # O ideal é que o fator de carga seja de, no máximo, 0.75
        #self._fator_carga = self._quantidade_elementos / self._tamanho 

    @property
    def tamanho(self):
        return self._tamanho

    @tamanho.setter
    def tamanho(self, tam):
        if not isinstance(tam, int):
            tam = int(tam)
        self._tamanho = tam
    
    def _sondagemLinear(self, indice_antigo):
        # Funcao de tratamento de colisao
        novo_indice = ((indice_antigo + 1) & 0x7FFFFFFF) % self._tamanho
        return novo_indice
    
    def _sondagemQuadratica(self, indice_antigo, iteracao):
        # Funcao de tratamento de colisao
        novo_indice = ((indice_antigo + (2 * iteracao + 1)) & 0x7FFFFFFF) % self._tamanho
        return novo_indice

    def _metodoDoResto(self, chave):
        # Funcao de hashing do metodo do resto
        espalhamento = (chave & 0x7FFFFFFF) % self._tamanho
        return espalhamento

    def _hashStrings(self, chave):
        # Funcao de hashing utilizada com strings
        soma = 0
        inicio = 0
        final = len(chave)
        while inicio < final:
            valor = ord(chave[inicio]) * (inicio + 1)
            soma = soma + valor
            inicio = inicio + 1
        indice = soma % self._tamanho
        return indice

    def _hashFolding(self, chave):
        # Funcao de hashing que divide a chave em tamanhos iguais (o ultimo pedaco possa ser que nao seja igual)
        chave = str(chave)
        parcela = ''
        inicio = 0
        final = len(chave)
        temporaria = 0
        while inicio < final:
            parcela = parcela + chave[inicio]
            if len(parcela) == 2 or inicio == (final - 1):
                parcela = int(parcela)
                temporaria = temporaria + parcela
                parcela = ''
            inicio = inicio + 1
        indice = temporaria % self._tamanho
        return indice

    def _hashQuadradoDoMeio(self, chave):
        # Funcao de hashing que eleva o item ao quadrado e depois extrai uma parte dos dígitos resultantes
        chave = chave ** 2
        chave = str(chave)
        inicio = (len(chave) - 1) // 2
        final = len(chave) - 1
        temporaria = ''
        while inicio < final:
            temporaria = temporaria + chave[inicio]
            inicio = inicio + 1
        temporaria = int(temporaria)
        indice = temporaria % self._tamanho
        return indice

    # Insercao e Busca utilizando Sondagem Linear
    
    def inserirElemento(self, chave, valor):
        if self._quantidade_elementos == self._tamanho:
            raise Exception('A Tabela Hash esta cheia.')
        elemento = ItemHash(chave, valor)
        indice = self._hashStrings(chave)
        #indice = self._hashStrings(chave)
        while self._tabela[indice] != None:
            if self._tabela[indice].chave == chave:
                break
            indice = self._sondagemLinear(indice)
        if self._tabela[indice] == None:
            self._tabela[indice] = elemento    
        self._quantidade_elementos = self._quantidade_elementos + 1
    
    def buscarElemento(self, chave):
        indice = self._hashStrings(chave)
        #indice = self._hashStrings(chave)
        while self._tabela[indice] != None:
            if self._tabela[indice].chave == chave:
                return self._tabela[indice].valor
            indice = self._sondagemLinear(indice)
        return None
    

    '''
    # Insercao e Busca utilizando Sondagem Quadratica
    def inserirElemento(self, chave, valor):
        if self._quantidade_elementos == self._tamanho:
            raise Exception('A Tabela Hash esta cheia.')
        elemento = ItemHash(chave, valor)
        indice = self._hashStrings(chave)
        #indice = self._hashStrings(chave)
        iteracao = 0
        while self._tabela[indice] != None:
            if self._tabela[indice].chave == chave:
                break
            indice = self._sondagemQuadratica(indice, iteracao)
            iteracao = iteracao + 1
        if self._tabela[indice] == None:
            self._tabela[indice] = elemento    
        self._quantidade_elementos = self._quantidade_elementos + 1

    def buscarElemento(self, chave):
        indice = self._hashStrings(chave)
        #indice = self._hashStrings(chave)
        iteracao = 0
        while self._tabela[indice] != None:
            if self._tabela[indice].chave == chave:
                return self._tabela[indice].valor
            indice = self._sondagemQuadratica(indice, iteracao)
            iteracao = iteracao + 1
        return None
    '''


    '''
    # Insercao e Busca Sem Tratamento de Colisão
    def inserirElemento(self, chave, valor):
        if self._quantidade_elementos == self._tamanho:
            raise Exception('A Tabela Hash esta cheia.')
        elemento = ItemHash(chave, valor)
        indice = self._metodoDoResto(chave)
        #indice = self._hashStrings(chave)
        if self._tabela[indice] == None:
            self._quantidade_elementos = self._quantidade_elementos + 1
        self._tabela[indice] = elemento    

    def buscarElemento(self, chave):
        indice = self._metodoDoResto(chave)
        #indice = self._hashStrings(chave)
        if self._tabela[indice].chave == chave:
            return self._tabela[indice].valor
        return None
    '''

    def restauraTabelaHash(self):
        # Metodo que restaura a Tabela Hash
        self._tabela = [None] * self._tamanho
        self._quantidade_elementos = 0
    
    def __setitem__(self, chave, valor):
        # Metodo que permite utilizar tabela_hash[chave] = valor, serve para inserir elemento na tabela
        self.inserirElemento(chave, valor)

    def __getitem__(self, chave):
        # Metodo que permite utilizar tabela_hash[chave] e é retornado o valor
        return self.buscarElemento(chave)

    def __len__(self):
        # Metodo que retorna o tamanho da tabela através do len(tabela_hash)
        return self._quantidade_elementos

    def __repr__(self):
        # Metodo que mostra a tabela hash para o desenvolvedor no modo interativo do Python
        return str(self)
    
    def __str__(self):
        # Metodo que mostra a tabela hash para o usuário através da função print()
        representacao = ''
        for i in range(0, self._tamanho):
            if self._tabela[i] != None:
                representacao = representacao + f'{self._tabela[i].chave} '
        return representacao        

    def __del__(self):
        return
