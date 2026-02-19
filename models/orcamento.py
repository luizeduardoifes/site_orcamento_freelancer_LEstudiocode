from dataclasses import dataclass

@dataclass
class Orcamento:
    nome: str
    email: str
    whatsapp: str
    tipo_servico: str
    descricao: str
    prazo_entrega: str