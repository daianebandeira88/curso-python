ficha=list()
while True:
    nome=str(input('nome'))
    nota1=float(input('nota1'))
    nota2=float(input('nota2'))
    media=(nota1+nota2)/2
    ficha.append([nome,[nota1,nota2],media])
    resp=str(input('quer continuar s/n ?'))
    if resp in 'n':
        break
print('-_'*40)
print(f'{"No.":<5} {"nome":<10} {"media":>8}')
print('-_'*40)
for i ,a  in enumerate(ficha):
    print(f'{i:<5}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*45)
    opc=int(input('mostrar notas de qual aluno? (999 pra parar)'))
    if opc == 999:
        print('      ----finalizando----')
        break
    if opc <= len(ficha)-1:
        print(f'notas de {ficha[opc][0]} sao {ficha[opc][1]}')
print('>>>>>> volte sempre >>>>>>')

