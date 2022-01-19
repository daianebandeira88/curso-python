lista=[[],[]]
for c in range(1,8):
    n=int(input(f'digite o {c}ª  numero'))
    if n % 2==0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print('='*45)
print(f'os valores pares digitados foeam {sorted(lista[0])}')
print(f'os numeros impares digitados foram {sorted(lista[1])}')
