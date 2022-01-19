n=int(input('digite um numero inteiro'))
print('escolha a base de conversão')
e=input('digite :\n [1] para binario;\n [2] para octal;\n [3] para hexadecimal\n')
if e == '1':
    print('em binario o numero é {}'.format(bin(n)))
elif e == '2':
    print('em octal o numero é {}'.format(oct(n)))
elif e== '3':
    print('o numero em hexadecimal é {}'.format(hex(n)))
else:
    print('opçao invalida , tente novamente')
