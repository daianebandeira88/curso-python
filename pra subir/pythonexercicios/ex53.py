f=input('digite a frase')
fse=f.replace(' ','')
ftm=fse.lower()
fi=ftm[::-1]
print(' {} invertida é {}'.format(f,fi))
if fi == ftm:
    print('sim é palindromo')
else:
    print('nao é palindromo')