import pytest
import sqlite3

@pytest.fixture
def db_connection():
    """Cria e fecha conexão com banco de dados em memória."""
    connection = sqlite3.connect(":memory:")
    yield connection
    connection.close()

@pytest.fixture
def setup_database(db_connection):
    """Cria tabelas, trigger e view no banco de dados."""
    cursor = db_connection.cursor()
    
    # Criando tabelas
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, user_id INTEGER, item TEXT, FOREIGN KEY (user_id) REFERENCES users(id))")
    cursor.execute("CREATE TABLE logs (id INTEGER PRIMARY KEY, action TEXT)")
    
    # Criando view
    cursor.execute("CREATE VIEW user_orders AS SELECT users.name, orders.item FROM users INNER JOIN orders ON users.id = orders.user_id")
    
    # Criando trigger
    cursor.execute("CREATE TRIGGER order_insert AFTER INSERT ON orders BEGIN INSERT INTO logs (action) VALUES ('Novo pedido registrado'); END;")
    
    db_connection.commit()
    cursor.close()