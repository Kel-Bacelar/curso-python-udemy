# if / elif    / else
# se /  se não se / se não

"""
entrada = input('Você quer "entrar" ou "Sair"? ')

if entrada == 'entrar':
    print(f'Você entrou no sistema')
elif entrada == 'sair':
    print('Você saiu do sistema')

    print(12345)
else:
    print('Você digitou algo nada a ver!')

print('Fora dos blocos')
"""
condicao1 = False
condicao2 = False
condicao3 = False
condicao4 = True

if condicao1:
    print(f'codigo para condição 1')
elif condicao2:
    print(f'codigo para  condição 2')
elif condicao3:
    print(f'condigo para  condição 3')
elif condicao4:
    print(f'condigo para condição 4')
else:
    print(f'nenhuma condição atendida')

if 10 == 10:
    print(f'Esse é outro if')

print(f'Isso esta fora dos blocos IF')


