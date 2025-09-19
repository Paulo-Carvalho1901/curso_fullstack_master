"""Escopo de variáveis"""

"""
as variáveis globais

as variáveis locais
"""

x = 5 # global

def funcao():
    x = 3 # local
    print('Valor do variáveil local', x)

funcao()
print('Valor da variável global', x)


# Má pratica para declarar variáveis

y = 'Gabriel' # nome
z = 1.74 # altura
t = '000.000.000-00' # cpf
l = 23 # idade

# Melhor pratica para para declarar variáveis

nome = 'Gabriel'
altura = 1.74
cpf = '000.000.000-00'
idade = 23
