import random


n1 = str(input('Inform o nome do primeiro aluno: '))
n2 = str(input('infomre o nome do seundo aluno:'))
n3 = str(input('Infomr o nome do terceiro aluno:'))
n4 = str(input('informe o nome do quarto aluno:'))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('o aluno escolhido foi {}'.format(escolhido))