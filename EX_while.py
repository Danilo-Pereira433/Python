nome = input('Digite o seu nome: ')
indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'•{letra}'
    indice += 1

novo_nome += '•'
print(f'nome antigo {nome}')
print(f'nome novo {novo_nome}')