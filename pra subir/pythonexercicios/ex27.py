n=str(input('digite seu nome completo')).strip()
nome=n.split()
print('seu primeiro nome é {} '.format(nome[0],))
print('e seu ultimo nome é {}'.format(nome[len(nome)-1]))
