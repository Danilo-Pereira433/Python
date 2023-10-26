while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('\033[;31mUm ou ambos os números digitados são inválidos.\033[m')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('\033[;31mOperador inválido.\033[m')
        continue

    if len(operador) > 1:
        print('\033[;31mDigite apenas um operador.\033[m')
        continue

    print('Realizando sua conta. Confira o resultado abaixo: ')

    if operador == '+':
        print(f'\033[;32m{num_1_float} + {num_2_float} =\033[;36m',
              num_1_float+num_2_float)
    elif operador == '-':
        print(f'\033[;32m{num_1_float} - {num_2_float} =\033[;36m',
              num_1_float-num_2_float)
    elif operador == '/':
        print(f'\033[;32m{num_1_float} / {num_2_float} =\033[;36m',
              num_1_float/num_2_float)
    elif operador == '*':
        print(f'\033[;32m{num_1_float} * {num_2_float} =\033[;36m',
              num_1_float*num_2_float)
    else:
        print('Nunca deveria ter chegado aqui. (⊙_⊙;)')

    sair = input('\033[mDeseja sair? [s]im: ').lower().startswith('s')

    if sair is True:
        print(f'''{'▬'*50}
\033[;33mVocê saiu!\033[m''')
        break
