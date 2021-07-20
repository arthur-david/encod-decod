from arvore_binaria import *

f = open("../arquivos/preordem.txt", "r")
pre = f.readline()
f.close()

arvore = ArvoreBinaria()
arvore.inicializar()
arvore.construtor(pre)

f = open("../arquivos/senhacodificada.txt", "r")
senha_cod = f.readline()
f.close()

senha_decod = ""
for i in range((len(senha_cod)//5)):
    s = senha_cod[i*5:(i+1)*5]
    senha_decod += arvore.consultar(s)

f = open("../arquivos/senhadecodificada.txt", "w")
f.write(senha_decod)
f.close()

print(senha_decod)