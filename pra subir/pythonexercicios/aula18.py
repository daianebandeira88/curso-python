galera=[['joao',33], ['hector',13],['daiane',30], ['kako',24]]
#print(galera[0][0])

for p in galera:
    #print(p[0])

  print(f'{p[0]} tem {p[1]} anos de idade')

    #ex2
galera2=[]
dado=[]
for c in range(0,3):
   dado.append(str(input('nome')))
   dado.append(int(input('idade')))
   galera.append(dado[:])
   dado.clear()
print(galera)