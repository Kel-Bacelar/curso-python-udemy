"""
Exercício
peça ao usuario para digitar seu nome
peça ao usuario para digitar sua idade
se nome e idade forem digitados:
    Exiba:
         seu nome é {nome}
         seu nome invertido é {nome invertido}
         se o nome contem (ou não) espaços
         seu nome tem {n} letras
         A primeira letra do seu nome é {letra}
         A ultima letra do seu nome é {letra}
    Se nada for digitado em nome ou idade:
       exiba "Desculpe, vo^ce deixou campos vazios."
"""
nome = input('digite seu nome:')
idade = input('digite sua idade: ')

if nome and idade:
    print(f'seu nome é {nome}')
    print(f'seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('seu nome contém espaços')
    else:
        print('seu nome não contem espaços')
    print(f'seu nome tem {len(nome)} letras')
    print(f'a primeira letra do seu nome é {nome[0]}')
    print(f'a ultima letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios')


    

