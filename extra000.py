preço = float(input('Digite o preço do produto: R$'))
desconto = preço - (preço * 10 / 100)
aumento = preço + (preço * 20 / 100)
print ('o preço de R${:.2f} sendo pago a vista tera 10% de desconto que resulta em R${:.2f}, mas se for pago parcelado tera 20% de aumenta no que resultará R${:.2f}'.format(preço, desconto, aumento))
