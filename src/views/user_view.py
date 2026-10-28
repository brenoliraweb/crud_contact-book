from services import user_service as service

def register_user():
    print('\n=== Novo Usuário ===\n')

    name = input('Nome: ').strip()
    contact = input('Contato: ').strip()

    try:
        service.register_user(name, contact)
        print('\nUsuário cadastrado com sucesso!')
    except ValueError as e:
        print(f'\nErro ao cadastrar: {e}')

def get_users():
    print('\n=== Lista de Usuários ===\n')

    users = service.list_users()

    if not users:
        print('Nenhum usuário cadastrado.')
        return

    for user in users:
        print(f"ID: {user['id_user']} | Nome: {user['name']} | Contato: {user['contact']}")

def update_user():
    print('\n=== Atualizar Usuário ===\n')

    try:
        id_user = int(input('Digite o ID do usuário: ').strip())
    except ValueError:
        print('\nErro: O ID precisa ser um número inteiro.')
        return

    contact = input('Digite o novo contato: ').strip()

    try:
        service.update_contact(id_user, contact)
        print('\nContato atualizado com sucesso.')
    except ValueError as e:
        print(f'\nErro ao atualizar: {e}')

def delete_user():
    print('\n=== Deletar Usuário ===\n')

    try:
        id_user = int(input('Digite o ID de usuário: ').strip())
    except ValueError:
        print('\nErro: O ID precisa ser um número inteiro.')
        return

    try:
        service.delete_user(id_user)
        print('\nUsuário deletado com sucesso.')
    except ValueError as e:
        print(f'\nErro ao deletar: {e}')