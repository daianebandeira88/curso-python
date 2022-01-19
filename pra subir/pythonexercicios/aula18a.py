totma=totme=0
galera=[]
dado=[]
for c in range(0,3):
   dado.append(str(input('nome')))
   dado.append(int(input('idade')))
   galera.append(dado[:])
   dado.clear()
print(galera)
print(dado)
for p in galera:
   if p[1] >= 21:
      totma +=1
      print(f'{p[0]} é maior de idade')
   else:
      print(f'{p[0]} é menor de idade')
      totme +=1
print(f'temos {totma} maiores de idade e {totme} menores de idade')