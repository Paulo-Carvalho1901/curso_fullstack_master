# Operador ternaria
a = 5
b = 4
c = 2

# expresões condicionais

if b > a: print('b é maior que a') 
print('fora do código')

print('B') if b > a else print('A')

# aninhado if
if a > b:
    print('a')
    if a > c:
        print('a')
