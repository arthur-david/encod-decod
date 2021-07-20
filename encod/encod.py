from tabela_hash import *

fileI = open("../arquivos/caracteres.txt", "r")
carac = fileI.readline()
fileI.close()

carac = list(carac)

codificador = Hash(len(carac))

for c in carac:
    codificador.insere(c)

codificador.mostrar_hash()

fileO = open("../arquivos/chave.txt", "w")
for i in range(32):
    valor = codificador.itens[i].valor
    binario = bin(i)
    binario = binario.replace("0b", "")
    if len(binario) < 5:
        s = ""
        for j in range(5-len(binario)):
            s += "0"
        binario = s + binario

    if i == 31:
        fileO.write("'{}', '{}'".format(valor, binario))
    else:
        fileO.write("'{}', '{}', ".format(valor, binario))

fileO.close()
