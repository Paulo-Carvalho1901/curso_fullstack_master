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
# 01 - área do retangulo


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

print()
print()

# 03 - se o produto que você quer avaliar custo (??) reais 
# qual será o valor do mesmo com desconto de (??)
print("Exercício 03 - Calcule o seu produto com desconto aplicado")
print(" ")
preco_produto = input('Quanto custa o seu produto? ')
desconta = input('Quanto o valor do desconto? ')

desconto = float(preco_produto) * float(desconta) / 100
preco_final = float(preco_produto) - desconto
print(" ")
print(f'O preço do produto com desconto é {preco_final}')


print()
print()

print("Exercício 04 - Calcule a area de um circulo")
print(" ")
raio = input("Qual e o raio do circulo? ")
area = 3.141592 * float(raio) ** 2
print(" ")
print(f"A area do seu circulo e {area}")

print(" ")
print(" ")
