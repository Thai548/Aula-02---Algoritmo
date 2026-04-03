# Crie um programa, que receba um número e mostre na saída o seu o dobro, o triplo e o  seu quadrado.

Valor = float(input ('Informe um valor:'))
Dobro = Valor * 2
Triplo = Valor * 3
Quadrado = Valor ** 2   

print(f'Valor Desejado: {Valor}')
print(f'Dobro do Valor: {Dobro}')
print(f'Triplo do Valor: {Triplo}')
print(f'O valor ao quadrado: {Quadrado}')

# Implemente um algoritmo que leia "receba" 4 notas de um aluno, retire a média e mostre o resultado na tela.


nota1 = float(input ('Informe Nota 1:'))
nota2 = float(input ('Informe Nota 2:'))
nota3 = float(input ('Informe Nota 3:'))
nota4 = float(input ('Informe Nota 4:'))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"Nota média do Aluno:{media}")
