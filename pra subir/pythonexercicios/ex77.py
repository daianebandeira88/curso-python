t=('aprender','programar','linguagem',
   'python','praticar','estudar','daiane')
for i in t:
   print(f'\n na palavra {i.upper()} temos ' , end='')
   for letra in i:
      if letra.lower() in 'aeiou':
         print(letra , end=' ')