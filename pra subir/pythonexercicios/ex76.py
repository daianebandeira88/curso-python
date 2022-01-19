lista=('pão',0.50,'leite',2.50,
       'mortadela',4.10,'margarina',5.99,
       'café',8.50,'queijo',25.60)
print('-'*40)
print('         LISTAGEM DE PRODUTOS')
print('-'*40)
for pos in range(0,len(lista)):
    if pos % 2 == 0:
      print(f'{lista[pos]:.<25} ',end="")
    else:
        print(f'R$:{lista[pos]:>5.2f}')
print('-'*40)