# Operador logico "Not"
# Usado para inverter expressões
# not True = False
# not False = True


# Operadores IN e Not In
# Strigs são interaveis
# 0 1 2 3 4 5 
# K e l i n t o n

# nome = 'Kelinton'
# print(nome[0])
# print(nome[4])
# print('lin' in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontarar: ')

if encontrar in nome:
     print(f'{encontrar} está em {nome}')
else:
     print(f'{encontrar} não está em {nome}')
     

