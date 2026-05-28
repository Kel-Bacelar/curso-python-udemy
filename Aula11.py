# Operadores lógicos
# and (e) or (ou) not (não)
# and: todas as condições verdadeiras
# caso contrario saida será falsy
# tipo none representa um não valor 
# exemplos: (0) (0.0) ('') - falsy

entrada = input('[E]ntrar [S]aair')
senha_digitada = input(f'Senha: ')
senha_permitida = '123456'

if entrada == 'E'and senha_digitada == senha_permitida:
    print(f'Entrar')
else:
    print(f'Sair')