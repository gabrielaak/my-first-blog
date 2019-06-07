print('Oi, Djangogirls!')
if 3>2:
    print('3 é maior que 2')
else:
    print('2 não é maior que 2')
idade = 10
if idade<=12:
    print('Criança')
elif idade <=19:
    print('Adolescente')
elif idade <=60:
    print('Adulto')
else:
    print('Idoso')
nome='Gabriela'
def oi(nome):
    print('Oi! Tudo bem,' + nome + '?')
oi(nome)
família=['Takashi', 'Neli', 'Erika']
for nome in família:
    oi(nome)
