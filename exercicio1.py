nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')

if nome and idade:
    print('-'*50)
    print(f'''Seu nome é: {nome}
Seu nome invertido é: {nome[::-1]}''')

    espaco = ' '
    if espaco in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')

    print(f'''Seu nome tem {len(nome)} letras
A primeira letra do seu nome é: {nome[0]}
A última letra do seu nome é: {nome[-1]}''')
else:
    print('-'*50)
    print('Desculpe, você deixou campos vazios.')
