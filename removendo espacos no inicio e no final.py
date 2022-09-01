from posixpath import split


frase='''     Pessoal ta entrando lá e testando, ai hoje eu reseto ele se pa, ou quando o pessoal entrar
        curso em video de python                      '''
print(frase.strip())
# se eu colocar rstrip vai remover os espacos na direita 
# se colocar lstrip vai remover os espacos na esquerda
# e se colocar strip vai remover nas extremidaddes
print(frase[2:6]) 
print(frase.split())
print('-'.join(frase))
print(frase[6:])
print(frase.count('c'))
print(frase.replace('a','(9)'))
