dados = {'rex':['biscoito','ração','agua'], 'fifi':['ração','agua']}
caes = list(dados.keys())
j = 0
while j < len(caes):
    cao = caes[j]
    print(' a ultima refeição do %s foi:'% cao)
    i = 0
    while i < len(dados[cao]):
        print(dados[cao][i])
        i += 1
    print("")
    j += 1
