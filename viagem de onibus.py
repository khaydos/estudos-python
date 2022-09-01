## passagem de ônibus  
v = float(input('informe a qunantidade de Km da viagem : '))
if v >= 200:
    vl = (v * 0.5)
    print('O valor a ser pago na viagem e {} R$ '.format(vl))
else:
    v2 = (v * 0.45)
    print('O valor a ser pago na viagem e {} R$'.format(v2))
