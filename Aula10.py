primeiro_valor = input('digite um valor: ')
segundo_valor = input('digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor} é maior que {segundo_valor}!')
elif primeiro_valor == segundo_valor:
    print(f'{primeiro_valor} são iguais {segundo_valor}!')
elif primeiro_valor < segundo_valor:
    print(f'{segundo_valor} é maior que {primeiro_valor}')
else:
    print(f'Você não digitou valor valido!')

