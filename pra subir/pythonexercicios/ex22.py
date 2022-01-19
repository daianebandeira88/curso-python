n=(input('digite seu nome completo')).strip()
m=(n.upper())
mi=(n.lower())

div=n.split()
print('o nome com todas maiusculas fica: {}\n  com todas minisculas {} '.format(m,mi))
pr=len(div[0])
print(' total de caracteres sem espaços é  ', (len(n)-n.count(' ')))
print('seu primeiro nome {} e tem {} letras'.format(div[0],pr))
