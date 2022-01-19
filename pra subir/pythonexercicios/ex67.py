c=0
while True:
    print('-'*35)
    n=int(input('quer ver a tabuada de qual numero?'))
    print('-'*35)
    if n<0:
        break

    for c in range(0,11):
      print(c,'*',n,'=',n*c)

print('programa encerrado')