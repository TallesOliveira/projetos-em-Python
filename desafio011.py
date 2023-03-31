larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt
print('A area das dimensões {} x {} resultam em {}m²'.format(larg, alt, area))
tinta = area / 2
print ('para pintar a parede será necessario {} litros de tinta'.format(tinta))
