s=''
while s != 'm' and s !='f':
    s=str(input('qual seu sexo? [ m / f ]:')).lower()

    if s == 'm':
       print('vc é do sexo masculino')
    if s == 'f':
        print('vc é do sexo feminino')


