import os
lista = []

while True:
    escolha = input(f'Selecione uma opção\n[i]nserir [a]pagar [l]istar:').upper()
    escolhas_permitidas = 'IAL'

    if escolha not in escolhas_permitidas:
        os.system('cls')
        print('Está não é uma opção válida!!!')

    if len(escolha) > 1:
        os.system('cls')
        print('Digite apenas uma opção!!!')  

    if escolha == 'I':
        os.system('cls')
        adicionar = input('O que você deseja inserir na lista? ')
        lista.append(adicionar)  

    if escolha == 'A':
        indice_apagar = input('Escolha o índice para apagar: ')
        indice_apagar = int(indice_apagar)
        try:
            os.system('cls') 
            del(lista[indice_apagar])
            print(f'Índice {indice_apagar}, apagado com sucesso')
        except ValueError:
            os.system('cls') 
            print('Digite um número inteiro!!!')
        except IndexError:
            os.system('cls') 
            print('Esse índice não existe!!!')
        except Exception:
            os.system('cls')
            print('Erro desconhecido!!!')

    if escolha == 'L':
        if bool(lista) == False:
            os.system('cls') 
            print('A lista está vazia!!!')
        else:
            os.system('cls') 
            for indice, nome in enumerate(lista):
                print(indice, nome)
