from repositories import user_repository as repo

def _validate_name(name):
    username = name.strip()

    if not username:
        raise ValueError('O nome não pode ficar vazio.')

    if len(username) > 250:
        raise ValueError('O nome deve ter no máximo 250 caracteres.')

    return username

def _validate_contact(contact):
    user_contact = contact.strip()

    if not user_contact:
        raise ValueError('O contato não pode ficar vazio.')

    return user_contact

def register_user(name, contact):
    username = _validate_name(name)
    user_contact = _validate_contact(contact)

    new_user = {
        'name': username,
        'contact': user_contact
    }

    new_user['id_user'] = repo.insert(username, user_contact)

    return new_user

def list_users():
    return repo.get()

def update_contact(id_user, contact):
    user_contact = _validate_contact(contact)

    updated_rows = repo.update(id_user, user_contact)

    if updated_rows == 0:
        raise ValueError(f'Nenhum usuário encontrado com esse id: {id_user}')

    return {'id_user': id_user, 'contact': user_contact}

def delete_user(id_user):
    delete_data = repo.delete(id_user)

    if delete_data == 0:
        raise ValueError(f'Nenhum usuário encontrado com esse id: {id_user}')