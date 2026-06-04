"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver
4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, 
escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""
user_name = input('Digite o seu nome: ')

if len(user_name) <= 4:
    print('seu nome é pequeno!')
elif 5 <= len(user_name) <= 6:
    print('seu nome é normal!')
elif len(user_name) > 6:
    print('Seu nome é grande!')
else:
    print('Erro: você digitou algum caractere invalido!')  
    
