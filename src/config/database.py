import os
import psycopg
from psycopg.rows import dict_row
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    """
        Realiza a conexão com o banco de dados
    """

    conn = psycopg.connect(
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT', '5432'),
        dbname=os.getenv('DB_NAME'),
        password=os.getenv('DB_PASSWORD'),
        user=os.getenv('DB_USER'),
        sslmode=os.getenv('DB_SSLMODE', 'require'),
        channel_binding=os.getenv('DB_CHANNEL_BINDING', 'require'),
        row_factory=dict_row
    )

    return conn

def test_connection():
    """
        Realiza o teste para saber se o banco de dados responde
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT 1;')

    print('Conexão realizada com sucesso!')

if __name__ == '__main__':
    test_connection()