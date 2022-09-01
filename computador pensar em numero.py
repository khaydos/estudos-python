import random

n = random.randint(1, 5)
n1 = int(input('informe um numero: '))
if n == n1:
    print('seu numero foi {} e o numero do computador foi {} parabens voce acertou! '.format(n1, n))
else:
    print('seu numero foi {} e o do computador foi {} voce errou, mais sorte na proxima! '.format(n1, n))
