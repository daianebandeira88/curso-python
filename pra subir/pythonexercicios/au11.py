# calculando o imc
nomePaciente = input('digite o nome do paciente')
peso = float(input('digite o peso do paciente'))
altura = float(input('digite a altura do paciente'))

imc = peso / (altura ** 2)
print('o imc do paciente {} é {:.2f} '.format(nomePaciente, imc))
