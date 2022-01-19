n=input('digite seu nome')
if n == 'daiane' :
    print('que nome lindo !')
elif n in ' ana claudia jessica luana':
    print('belo nome feminino')
elif n== 'jose' or n=='maria' or n=='paulo':
    print('seu nome é bem popular !')
else:
    print('seu nome é normal')
print('tenha um bom dia {} !'.format(n))