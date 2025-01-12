import json


def carregar_estoque():
    try:
        with open('estoque.txt', 'r') as arquivo:
            estoque = json.load(arquivo)
        print('Estoque carregado com sucesso.')
    except FileNotFoundError:
        print('Arquivo de estoque não encontrado. Criando um novo estoque...')
        estoque = {}
    return estoque

def salvar_estoque(estoque):
    with open('estoque.txt', 'w') as arquivo:
        json.dump(estoque, arquivo, indent=4)
    print('Estoque salvo com sucesso.')

def adicionar_atualizar_estoque(estoque):
    while True:
        try:
            produto = input('Digite o nome do produto que deseja adicionar ao estoque: ').strip().capitalize()
            if not produto:
                raise ValueError('O nome do produto precisa ser preenchido.')

            quantidade = float(input('Digite a quantidade do produto que deseja adicionar: '))
            if quantidade < 0:
                raise ValueError('A quantidade precisa ser um valor positivo.')

            if produto in estoque:
                estoque[produto] += quantidade
            else:
                estoque[produto] = quantidade

            print(f'Produto "{produto}" atualizado com sucesso. Quantidade atual: {estoque[produto]}.')

            continuar_adicionando = input('Deseja adicionar outro produto? [S/N] ').strip().upper()
            if continuar_adicionando != 'S':
                break
        except ValueError as e:
            print(f'Erro: {e}')
    return estoque

def remover_produtos_indisponiveis(estoque):
    while True:
        print(f'\nEstoque atual: {estoque}')
        produto = input('Digite o nome do produto a ser removido (ou "sair" para encerrar): ').capitalize()
        if produto == 'Sair':
            break
        if produto in estoque:
            del estoque[produto]
            print(f'O produto "{produto}" foi removido com sucesso.')
        else:
            print(f'O produto "{produto}" não está no estoque.')
    return estoque

def consultar_estoque(estoque):
    escolha = input('Digite "Estoque" para listar todos os produtos ou o nome de um produto específico: ').capitalize()
    if escolha == 'Estoque':
        for item, quantidade in estoque.items():
            print(f'{item}: {quantidade} unidades disponíveis.')
    elif escolha in estoque:
        print(f'{escolha}: {estoque[escolha]} unidades disponíveis.')
    else:
        print(f'{escolha} não está no estoque.')

def menu_programa(estoque):
    print('Bem-vindo ao programa de gerenciamento de estoque.')
    while True:
        print('\nEscolha uma das funcionalidades:')
        print('1 - Adicionar ou atualizar o estoque.')
        print('2 - Remover produtos do estoque.')
        print('3 - Consultar o estoque.')
        print('Sair - Encerrar o programa.')
        opcao_menu = input('Escolha: ').strip().lower()

        if opcao_menu == '1':
            estoque = adicionar_atualizar_estoque(estoque)
        elif opcao_menu == '2':
            estoque = remover_produtos_indisponiveis(estoque)
        elif opcao_menu == '3':
            consultar_estoque(estoque)
        elif opcao_menu == 'sair':
            salvar_estoque(estoque)
            print('Encerrando o programa...')
            break
        else:
            print('Opção inválida. Tente novamente.')

# Carrega o estoque ao iniciar o programa
estoque = carregar_estoque()
menu_programa(estoque)
