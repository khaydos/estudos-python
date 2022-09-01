##aumento de salario

s = float(input('informe seu salario :'))
if s > 1250:
    aumento = (1250 * 15/100)
    sa = (aumento+s)
    print('Seu salario {} R$ com o aumento de 10 %' ' e {} R$'.format(s, sa))
else:
    aumento2 = (s * 15/100)
    s2 = (aumento2+s)
    print('seu salario {} R$ com o aumento de 15%" ficou {} R$'.format(s, s2))
