from typing import Optional
from fastapi import FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from models.orcamento import Orcamento
from repo.orcamento_repo import criar_tabela_orcamento, inserir_orcamento

criar_tabela_orcamento()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("menu.html", {"request": request})



@app.get("/servicos")
async def read_servicos(request: Request):
    return templates.TemplateResponse("servicos.html", {"request": request})

@app.get("/formulario_orcamento")
async def read_formulario_orcamento(request: Request):
    return templates.TemplateResponse("formulario_orcamento.html", {"request": request})

@app.post("/formulario")
async def submit_formulario_orcamento(
    request: Request,
    nome: Optional[str] = Form(None),
    email: Optional[str] = Form(None),
    whatsapp: Optional[str] = Form(None),
    tipo_servico: Optional[str] = Form(None),
    descricao: Optional[str] = Form(None),
    prazo_entrega: Optional[str] = Form(None)
):
    orcamento = Orcamento(
        nome=nome,
        email=email,
        whatsapp=whatsapp,
        tipo_servico=tipo_servico,
        descricao=descricao,
        prazo_entrega=prazo_entrega
    )
    inserir_orcamento(orcamento)
    return templates.TemplateResponse("formulario_orcamento.html", {"request": request, "sucesso": "Orçamento enviado com sucesso!\nPode entrar em contato conosco para mais informações ou acertos de pagamentos."})
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)