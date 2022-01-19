km=float(input('quantos km foram rodados?'))
dias=int(input('por quantos dias o carro esteve locado?'))
to=(dias*60)+(km*0.15)
print('o total do aluguel sera R${:.2f}'.format(to))