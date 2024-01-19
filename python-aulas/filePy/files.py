## "r" - Read - Leitura dos arquivos
## "a" - Append - Abre o arquivo e cria caso não exista
## "w" - Write - Abre o arquivo para escrita
## "x" - Create - Cria o arquivo
##
import os.path
import datetime

## Criando os Arquivos

## Abertura dos arquivos
file1 = open("file1.txt")
file2 = open("file2.txt", "w")
file3 = open("file3.txt", "r")

### Caminho o Arquivo
pathString = "file1.txt"
absPath = os.path.abspath(pathString)
print(absPath)
#
#### Fechando o Arquivo
file1.close()
file2.close()
file3.close()
#
#### Imprimindo o conteudo
path = "file1.txt"
file = open(path)
print(type(file))
for line in file:
    print(line)
file.close
#
####3 Editando o arquivo
#path = "file2.txt"
#file = open(path,"a")
#i = cont
#for i in range(5):
#    x = datetime.datetime.now()
#    file.write("Linha "+str(i)+" - "+str(x)+"\n")
#file.close
#file = open(path,"r")
#print(file.read())
#
### Remove o arquivo
#if os.path.exists("demofile.txt"):
#  os.remove("demofile.txt")
#else:
#  print("Arquivo não existe")