-- Criando a tabela users
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT
);

-- Criando a tabela orders
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    item TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Criando a tabela logs
CREATE TABLE logs (
    id INTEGER PRIMARY KEY,
    action TEXT
);

-- Criando a trigger para registrar inserções em orders
CREATE TRIGGER order_insert
AFTER INSERT ON orders
BEGIN
    INSERT INTO logs (action) VALUES ('Novo pedido registrado');
END;

-- Criando a view para exibir usuários e seus pedidos
CREATE VIEW user_orders AS
SELECT users.name, orders.item
FROM users
INNER JOIN orders ON users.id = orders.user_id;