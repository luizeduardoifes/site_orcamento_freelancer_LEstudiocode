from typing import Optional

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
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

@app.get("/menu", response_class=HTMLResponse)
async def menu(request: Request):
    sucesso = request.query_params.get("sucesso")
    return templates.TemplateResponse(
        "menu.html",
        {
            "request": request,
            "sucesso": sucesso,
            "abrir_modal": False
        }
    )

@app.post("/formulario_orcamento", response_class=HTMLResponse)
async def formulario_orcamento(
    nome: str = Form(None),
    email: Optional[str] = Form(None),
    whatsapp: Optional[str] = Form(None),
    tipo_servico: str = Form(None),
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

    return RedirectResponse(url="/menu?sucesso=Orçamento enviado com sucesso!", status_code=303)

@app.get("/servicos.html")
async def read_servicos(request: Request):
    return templates.TemplateResponse("servicos.html", {"request": request})



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)