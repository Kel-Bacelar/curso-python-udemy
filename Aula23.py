#Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
#descrito, exiba a saudação apropriada 
#Ex. Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

hora_do_usuario = input('Por favor, digite a hora atual (apenas o número de 0 a 23): ')

if hora_do_usuario.isdigit():

    if 0 <= int(hora_do_usuario) <= 11:
        print('Bom dia!')
    elif 12 <= int(hora_do_usuario) <= 17:
        print('Boa tarde!')
    elif 18 <= int(hora_do_usuario) <= 23:
        print('Boa noite!')
    else:
        print('Erro: A hora deve ser um número entre 0 e 23!')

else:
    print('Erro: você não digitou um número inteiro!')
