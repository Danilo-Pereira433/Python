# FORMA QUE EU RESOLVI
# ------------------------------------------
# nome = input('Digite seu primeiro nome: ')

# tamanho_do_nome = len(nome)

# if tamanho_do_nome <= 4 :
#     print('Seu nome é curto.')
# elif tamanho_do_nome <= 6 :
#     print('Seu nome é normal.')
# else :
#     print('Seu nome é muito grande.')

# FORMA RESOLVIDA PELO PROFESSOR 1º
#----------------------------------------------
nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')