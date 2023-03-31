dias = int (input('Quantos dias o carro ficou alugado? '))
km = float (input('Qauntos km percorrido com o carro? '))
pagar = (dias * 60) + (km * 0.15)
print ('O total a pagar é R${:.2f}'.format(pagar))
