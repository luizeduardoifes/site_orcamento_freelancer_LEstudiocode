CREATE_TABLE_ORCAMENTO = """
CREATE TABLE IF NOT EXISTS orcamento (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    whatsapp TEXT NOT NULL,
    tipo_servico TEXT NOT NULL,
    descricao TEXT NOT NULL,
    prazo_entrega TEXT NOT NULL
);
"""

INSERT_ORCAMENTO = """
INSERT INTO orcamento (nome, email, whatsapp, tipo_servico, descricao, prazo_entrega)
VALUES (?, ?, ?, ?, ?, ?);
"""