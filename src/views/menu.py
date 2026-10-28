from views.user_view import (register_user, get_users, update_user, delete_user)

def start_menu():
    while True:
        try:
            message = '''
            \n === Lista de Usuários ===

            * [1] - Cadastrar usuário
            * [2] - Listar usuários
            * [3] - Atualizar usuário
            * [4] - Deletar usuário
            * [0] - Sair\n
            '''

            print(message)

            option = int(input('Escolha uma opção: ').strip())

            if option == 1:
                register_user()
            elif option == 2:
                get_users()
            elif option == 3:
                update_user()
            elif option == 4:
                delete_user()
            elif option == 0:
                print('\nSaindo do sistema...\n')
                exit()
            else:
                print('Opção inválida. Tente novamente.')

        except ValueError:
            print('Entrada inválida. Digite um número inteiro.')