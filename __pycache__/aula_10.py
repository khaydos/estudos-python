from string import printable


nome = str(input('Qual o seu nome ?'))
if nome == 'carlos':
    print('que nome lindo !')
else:
    print('Seu nome e tao normal!')
print('Bom dia, {}'.format(nome))
