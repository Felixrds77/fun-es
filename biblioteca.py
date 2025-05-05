#atividade01
def piramide (num):
    for z in range (1,num+1,1):
        for j in range(0,z):
            print(z, end=" ")
        print()
#atividade02
def  vogais (texto):
    contador = 0
    for x in texto:
        if x in texto:
            contador +=1
    print(contador)
#atividade03
def estoque (nome, quantidade, valor_unitario):
    valor_total= quantidade * valor_unitario
    return nome, valor_total
#atividade04
def numero (a):
    if a > 0:
        return "P"
    if a <0:
        return "N"
    else:
        return "Z"
#atividade05
def calculo (num1, num2):
    soma = num1 + num2
    print(soma)
#atividade06
def somar (*itens):
    soma = sum(itens)
    print(soma)
#atividade07
def ao_contrario (texto):
    contador = 0
    for x in range(len(texto)-1, -1, -1):
        if texto[x]!=" ":
            contador += 1
        print(contador)
        print(texto[x], end=" ")
#atividade08
def numerosUnicos (lista):
    novaLista = []
    for x in lista:
        if x not in novaLista:
            novaLista.append(x)
            print(novaLista)
def lista2 (lista):
    NovaLista=[]
    NovaLista=set(lista)
    print(NovaLista)
