# FORMA QUE EU RESOLVI
# ------------------------------------------
'''
numero = input('Digite um número inteiro: ')

if numero.isdigit():
    numero = int(numero)
    if (numero % 2) == 0:
        print('O número é par.')
    else:
        print('O número é ímpar.')
else:
    print('Não foi digitado um número inteiro!')
'''

# FORMA RESOLVIDA PELO PROFESSOR 1º
#----------------------------------------------
'''
entrada = input('Digite um número: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
else:
    print('Não foi digitado um número inteiro!')
'''
# FORMA RESOLVIDA PELO PROFESSOR 2º
#-----------------------------------------------
entrada = input('Digite um número: ')

try:
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
except:
    print('Não foi digitado um número inteiro!')