# Resposta exercicio 01
#Faça um programa que peça ao usuário para digitar um número inteiro,
#informe se este número é par ou ímpar. Caso o usuário não digite um numero inteiro, 
#informe que não é um número inteiro.

numero_int = input('digite um numero inteiro: ')

if numero_int.isdigit():
    
    if int(numero_int) % 2 == 0:
        print(f'O numero é PAR.')
    else:
        print(f'O numero é ÍMPAR.')

else: print(f'ERRO: você digitou um numero não inteiro!')
