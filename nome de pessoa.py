#//brincando com nome

nome = str(input('Informe seu nome completo :\n')).strip()
print('Analizando seu nome...')
print('seu nome em letras maiusculas e:  {}'.format(nome.upper()))
print('seu nome em minusculas e: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
separa= nome.split()
print('seu primeiro nome e - {} - e ele tem -{}- letras '.format(separa[0], len(separa[0])))