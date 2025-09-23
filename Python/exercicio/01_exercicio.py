"""
Exercicio - Python

Observação - Todos os exercícios devem utilizar a função input
de forma que o usuário possa determina os dados de entrada 

01 - área de um retangulo
02 - área de um quadrado
03 - se o produto que você quer avaliar custo (??) reais 
qual será o valor do mesmo com desconto de (??)
04 - área de um circulo
05 - conversão de reais para dorlar
06 - conversão de dolar para real
"""

print('=-' * 30)
# exercicio 01 - área do retangulo


print('Calcule a áreea de um retangulo.')

base = input('Qual o tamnho da base do seu retangulo')
altura = input('Qual o tamanho da altura do seu regulamento.')
area = float(base) * float(altura)

print(f'O seu retangulo possui area {area}')

print()
print()

# 02 - área de um quadrado
print("Exercício 02 - Calcule a area de um quadrado")
base_ou_altura = input("Qual o tamanho da base ou da altura do seu quadrado? ")
print(" ")
area = float(base_ou_altura) * 2
print(" ")
print(f'O seu quadrado possui area: {area} unidades de medida')