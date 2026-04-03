# salario = float(input('Informe o salário:'))
# bonus = float(input ('Informe o bônus:'))
# total_salario = salario + bonus

# print (f'Total:{total_salario}')



# valor = int(input('Valor atual:'))
# sucessor = valor + 1
# antecessor = valor - 1 


# print (f'Se o valor atual é {valor}, seu sucessor é {sucessor}, e seu antecessor é {antecessor}')

# # salario  + salario acrescentado de 15 %

salario = float(input('Informe seu salário: '))
Aumento = salario * 15/100 #(15%)
salario_atualizado = salario + Aumento

print(f'Valor do aumento: {Aumento:.2f}') 
print (f'Salário atualizado R$  {salario_atualizado}')
