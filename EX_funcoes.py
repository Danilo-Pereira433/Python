
def multiplicacao(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

def par_ou_impar(a):
    resposta = None
    if a%2 == 0:
        resposta = 'PAR'
    else:
        resposta = 'ÍMPAR'
    return resposta

mult = multiplicacao(3,3)

parOuImpar = par_ou_impar(mult)

print(f'O valor da multiplicação é: {mult}\nO número é:{parOuImpar}')