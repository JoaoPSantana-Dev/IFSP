import os
import sqlite3


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")

DB_PATH = os.path.join(
    DATA_DIR,
    "supermercado.db"
)


def get_connection():
    os.makedirs(DATA_DIR, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    conn.row_factory = sqlite3.Row

    conn.execute(
        "PRAGMA foreign_keys = ON"
    )

    return conn


def init_db():
    conn = get_connection()

    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            categoria TEXT NOT NULL,
            fabricante TEXT NOT NULL,
            unidade TEXT NOT NULL,
            preco REAL NOT NULL,
            estoque INTEGER NOT NULL DEFAULT 0
        );


        CREATE TABLE IF NOT EXISTS compras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT NOT NULL,
            data_hora TEXT NOT NULL,
            total REAL NOT NULL DEFAULT 0
        );


        CREATE TABLE IF NOT EXISTS itens_compra (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            compra_id INTEGER NOT NULL,

            produto_id INTEGER,

            produto_nome TEXT NOT NULL,

            quantidade INTEGER NOT NULL,

            preco_unitario REAL NOT NULL,

            subtotal REAL NOT NULL,

            FOREIGN KEY (compra_id)
                REFERENCES compras(id)
                ON DELETE CASCADE
        );
        """
    )

    conn.commit()

    conn.close()

