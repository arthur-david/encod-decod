chv = open("../arquivos/chave.txt", "r")
chaves = chv.readline()
chv.close()

chaves = chaves.split(", ")
for i in range(len(chaves)):
    chaves[i] = chaves[i].replace("'", "")

cod = dict()
for i in range(len(chaves)):
    if (i % 2) != 0:
        continue
    cod.update({chaves[i]: chaves[i+1]})

pwd = open("../arquivos/senha.txt", "r")
password = pwd.readline()
pwd.close()

pwd_cod = open("../arquivos/senhacodificada.txt", "w")
for s in password:
    pwd_cod.write(cod[s])
pwd.close()
