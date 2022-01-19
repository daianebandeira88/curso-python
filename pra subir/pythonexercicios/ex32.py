a=int(input('digite o ano'))
if a % 4 == 0 and a % 100!=0 or a % 400==0:
    print('ano {} é bissexto'.format(a))
else:
     print('o ano {} nao é bissesto'.format(a))
