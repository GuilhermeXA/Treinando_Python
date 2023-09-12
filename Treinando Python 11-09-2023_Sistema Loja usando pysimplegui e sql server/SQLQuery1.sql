use PythonSQL

CREATE TABLE produtos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    marca TEXT NOT NULL,
    preco REAL NOT NULL,
    quantidade INTEGER NOT NULL
);

select * from produtos;

