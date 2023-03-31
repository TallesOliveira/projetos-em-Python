salario = float (input('Digite seu salário: R$'))
novo = salario +  (salario * 15 / 100)
print ('Seu salário de R${:.2f} com 15% de aumento ficará R${:.2f}'.format(salario, novo))
