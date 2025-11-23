#Calculadora de quantidade mínimas necessárias de
# TUG's e potência de iluminação de cômodos quadriláteros paralelos

#Define o método para saber a quantidade de TUG's

from math import ceil

comodo = (input("O Cômodo a ser analizado é um destes?" \
"\nCozinha\nCopas\nCopas-cozinhas\nÁreas de serviço\nLavanderias\nou Locais análogos?"\
"\n(digite S para sim ou N para não) : "))

if comodo.lower() == "s":
    fator_perimetro = 3.5
else:
    fator_perimetro = 5

#Corrige o erro do programa ao digitar número com vírgula

lado1 = str(input("Em metros, qual o comprimento de uma das paredes? : "))
lado2 = str(input("Em metros, qual o comprimento da outra parede? : "))

tamanho1 = float(lado1.replace(",","."))
tamanho2 = float(lado2.replace(",","."))


#Define o que é perímero e área
perimetro = 2 * (tamanho1 + tamanho2)
area = tamanho1 * tamanho2 

#Define a quantidade de TUG's para o cômodo
tug = ceil(perimetro/fator_perimetro)

#Função para definir a potência de Iluminação para o cômodo
funcao = area - 6

tentativas = 0
while funcao > 0:
    funcao = funcao-4
    tentativas = tentativas+1

if funcao < 0:
    tentativas = tentativas-1

luzPotencia = 100+tentativas*60

# Mostra os resultados
print("A quantidade de TUG's necessária é", tug)
print("A potência de Iluminação necessária é de", luzPotencia,"VA")