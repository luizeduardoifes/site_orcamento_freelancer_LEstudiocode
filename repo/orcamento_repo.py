from database.database import criar_conexao
from models.orcamento import Orcamento
from sql.orcamento_sql import *


def criar_tabela_orcamento():
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(CREATE_TABLE_ORCAMENTO)
    conexao.commit()
    conexao.close()

def inserir_orcamento(orcamento: Orcamento) -> Orcamento:
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(INSERT_ORCAMENTO, (orcamento.nome, orcamento.email, orcamento.whatsapp, orcamento.tipo_servico, orcamento.descricao, orcamento.prazo_entrega))
    conexao.commit()
    conexao.close()
    return orcamento