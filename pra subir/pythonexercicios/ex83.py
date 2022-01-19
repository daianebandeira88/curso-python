ex=str(input('digite a expressão'))
pilha=[]
for simb in ex:
    if simb =='(':
       pilha.append('(')
    elif simb == ')':
        if len(pilha)> 0:
            pilha.pop()
        else:
           pilha.append(')')
           break
if len(pilha)==0:
    print('sua expressão é valida')
else:
    print('sua expressão é invalida')
