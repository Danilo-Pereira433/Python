import sys

cpf_enviado_usuario = '527.207.428.99' \
    .replace('.', '')\
    .replace(' ', '')\
    .replace('-', '')

entradad_e_sequencial = cpf_enviado_usuario == cpf_enviado_usuario[0] * len(cpf_enviado_usuario)

if entradad_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()


nove_digitos = cpf_enviado_usuario[:9]
contador_regrssivo_1 = 10

resultado_digito_1 = 0
for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regrssivo_1
    contador_regrssivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)

#Digito 2 -----------------------------------
dez_digitos = cpf_enviado_usuario[:10]
contador_regrssivo_2 = 11

resultado_digito_2 = 0
for digito_2 in dez_digitos:
    resultado_digito_2 += int(digito_2) * contador_regrssivo_2
    contador_regrssivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
print(digito_2)

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_usuario} é válido')
else:
    print('CPF inválido')