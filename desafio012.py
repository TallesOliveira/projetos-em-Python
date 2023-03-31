preço = float(input('Qual é o preço do produto? R$'))
desconto = preço - (preço*5/100)
print ('{:.2f}R$ com 5% de desconto fica {:.2f} reais'.format (preço, desconto))
