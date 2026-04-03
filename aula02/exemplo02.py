# # nome = "Maria"
# # idade = 18

# # print(f'Olá {nome}')
# # print (f'Você tem {idade} anos')

# # #----------------------------------------------

# # # Atividade Fixação 

# # nome = "Thainá"
# # bairro = "Ampliação"
# # Profissao = "Administradora"

# # print (f'Nome: {nome}')
# # print(f'Bairro: {bairro}')
# # print(f'Profissão: {Profissao}')

# # #------------------------------------------#

# # #Operadores

# # preco = 20
# # quantidade = 3
# # total = preco * quantidade 
# # print(f'O total é {total}')


# # #------------------------------------------#

# # salario = 1900
# # bonus = 500
# # total = salario + bonus 
# # print (f'Sálario Bruto do Colaborador: {total}')

#     #-----------------------------------------------#

# # Exemplo de entrada de valores pelo usuário:

# nome = input('Infomre o nome:')
# print (f'Olá {nome}!')


# # #Atividade Fixação 

# salario = float(input('Informe o salário:'))
# bonus = float(input ('Informe o bônus:'))
# total_salario = salario + bonus

# print (f'Total:{total_salario}')

# # string = texto  / float= Números decimais / int= Número inteiro / Boleano = True ou false

# #Cálculo de porentagem:

preco = float(input('Informe o preço: '))
quantidade = int(input('Qual a quantidade: '))
valor_total= preco * quantidade 
desconto = valor_total * 10 / 100   #(10/100 é porcentagem, pode usar também 0.1 que é 10%)
Valor_final = valor_total - desconto

print(f'Valor a pagar :{valor_total}')
print (f'Valor a pagar com desconto:  {Valor_final}')
