# FORMA QUE EU RESOLVI
# ------------------------------------------
'''
hora = input('Que horas são? ')
hora_int = int(hora)
if hora_int < 11:
    print('Bom dia!')
elif hora_int < 17:
    print('Boa tarde!')
else:
    print('Boa noite!')
'''
# FORMA RESOLVIDA PELO PROFESSOR 1º
#----------------------------------------------
entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde!')
    elif hora >= 18 and hora <= 23:
        print('Boa noite!')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')