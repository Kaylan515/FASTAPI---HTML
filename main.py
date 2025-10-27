# pip install fastapi uvicorn jinja2 python-multipart
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Lista de alunos")

#Definir a pasta onde está os html
templates = Jinja2Templates(directory="templates")

#Definir a pasta onde está os arquivos estaticos (CSS, Imagens e JS)
app.mount("/static", StaticFiles(directory="static"), name="static")


alunos = [
    {"nome": "Iago", "nota": 8.5},
    {"nome": "Murilo", "nota": 6.5},
    {"nome": "Joana", "nota": 9.5},
    {"nome": "Franscisco", "nota": 8.0},
]

#Rota principal
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.HTML",
        {"request": request, "lista_alunos": alunos}
    )