from html.entities import name2codepoint


n1 = float(input('digite a primeira nota :'))
n2 = float(input('digite a segunda nota :'))
m = (n1+n2)/2
print('a sua media e {:.1f}'.format(m))
print('PARABENS'if m >= 6 else 'estude mais')
