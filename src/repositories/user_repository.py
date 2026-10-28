from config.database import get_connection

def insert(name, contact):
    """
        Insere um novo usuário no banco de dados
    """

    script_sql = '''
        INSERT INTO users (name, contact) VALUES
            (%s, %s)
        RETURNING id_user;
    '''

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(script_sql, (name, contact))

            return cur.fetchone()['id_user']

def get():
    """
        Lista todos os usuários cadastrados no banco de dados
    """

    script_sql = '''
        SELECT * FROM users ORDER BY id_user;
    '''

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(script_sql)

            return cur.fetchall()

def update(id_user, contact):
    """
        Atualiza o contato de um usuário no banco de dados pelo ID
    """

    script_sql = '''
        UPDATE users
        SET contact = %s
        WHERE id_user = %s;
    '''

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(script_sql, (contact, id_user))

            return cur.rowcount

def delete(id_user):
    """
        Deleta um usuário do banco de dados pelo ID
    """

    script_sql = '''
        DELETE FROM users WHERE id_user = %s;
    '''

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(script_sql, (id_user,))

            return cur.rowcount