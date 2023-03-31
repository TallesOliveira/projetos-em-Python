metro = float(input('Digite o metro: '))
cm = (metro * 100)
mn = (metro * 1000)
dm = (metro * 10)
dam = (metro / 10)
hm = (metro / 100)
km = (metro / 1000)
print ('{} metros fica em: \nkm:{} \nhm:{} \ndam:{} \ndm:{} \ncm:{} \nmn:{}'.format(metro, km, hm, dam, dm, cm, mn))


