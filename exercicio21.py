salario = float (input('Qual o Salário do Funcionário? R$ '))
novo = salario + (salario * 15 / 100 )
print ('Um Funcionário que ganhava R${}, agora com 15% de aumento passa a receber R${}'.format(salario, novo))