tm20 = toi = h = 0

print('-' * 25)
print('  CADASTRANDO PESSOAS ')
print('-' * 25)
while True:
    id = int(input('digite a idade '))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('digite o sexo')).upper()
    if id >= 18:
        toi += 1
    if sex == 'M':
        h += 1
    if sex == 'f' and id < 18:
        tm20 += 1
    r = ' '
    while r not in "SN":
        r = str(input('quer continuar?[s/n]')).upper()
    if r == 'N':
        break

print(f' {toi} pessoas tem mais de 18 anos')
print(f'o total de homens foi {h}')
print(f'total de mulheres com menos de 20 anos {tm20}')
