import random
n1=input('primeiro aluno')
n2=input('segundo aluno')
n3=input('treceiro aluno')
n4=input('quarto aluno')
lista=[n1,n2,n3,n4]
ecolhido=random.choice(lista)
print('o escolhido foi {}'.format(ecolhido))