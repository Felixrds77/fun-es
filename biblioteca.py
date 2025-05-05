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
def