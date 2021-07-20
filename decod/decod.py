from arvore_binaria import *

chv = open("../arquivos/chave.txt", "r")
chaves = chv.readline()
chv.close()

chaves = chaves.split(", ")
for i in range(len(chaves)):
    chaves[i] = chaves[i].replace("'", "")

decod = dict()
for i in range(len(chaves)):
    if (i % 2) != 0:
        continue
    decod.update({chaves[i]: chaves[i+1]})

arvore = ArvoreBinaria()
arvore.inicializar()

keys = list(decod)

for k in keys:
    arvore.insere(k, decod[k])

r = arvore.pre_ordem(arvore.raiz)
pre = open("../arquivos/preordem.txt", "w")
pre.write(r)
pre.close()