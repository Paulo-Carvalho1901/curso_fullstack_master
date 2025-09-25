# 01 - Criar a variável

idade = int(input('Quantos anos você tem? '))
if idade < 16:
    print('menor')
elif idade > 18:
    print('Mair')
else:
    print('Emancipado.')


# 02 - Buscar a idade de nadador e classificar na tabela: 

idade = input("Ola nadador! quantos anos voce tem? ")

if int(idade) > 4 and int(idade) < 8:
    print('infantil A')
elif int(idade) > 7 and int(idade) < 11:
    print('infantil B')
elif int(idade) > 10 and int(idade) < 14:
    print('Juvenil A')
elif int(idade) > 13 and int(idade) < 18:
    print('Juvenilo B')
else:
    print('Você pertence ao grupo de natacao.')