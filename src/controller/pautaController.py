import os
from dotenv import load_dotenv
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from ..domain.models.pautaSchema import EmailSchema
from starlette.responses import JSONResponse
from fastapi import APIRouter

pauta = APIRouter(
  prefix="/pauta"
)

load_dotenv()

MAIL_USERNAME=os.getenv("MAIL_USERNAME")
MAIL_PASSWORD=os.getenv("MAIL_PASSWORD")
MAIL_FROM=os.getenv("MAIL_FROM")
MAIL_PORT=os.getenv("MAIL_PORT")
MAIL_SERVER=os.getenv("MAIL_SERVER")

conf = ConnectionConfig(
    MAIL_USERNAME = MAIL_USERNAME,
    MAIL_PASSWORD = MAIL_PASSWORD,
    MAIL_FROM = MAIL_FROM,
    MAIL_PORT = MAIL_PORT,
    MAIL_SERVER = MAIL_SERVER,
    MAIL_STARTTLS = False,
    MAIL_SSL_TLS = True,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)


@pauta.post("/email")
async def simple_send(email: EmailSchema) -> JSONResponse:
    # Use os campos adicionados ao objeto EmailSchema para preencher o corpo do e-mail
    html = f"""
    <html>
    <head></head>
    <body>
        <h1>Tema: {email.tema}</h1>
        <p>Descrição: {email.descricao}</p>
        <p>Quando: {email.quando}</p>
        <p>Local: {email.local}</p>
        <p>Responsável: {email.responsavel}</p>
        <p>Telefone do Responsável: {email.telefone_responsavel}</p>
        <p>Email para Contato: {email.email_contato}</p>
    </body>
    </html>
    """

    message = MessageSchema(
        subject="Sugestão de Pauta",
        recipients=email.recipients,
        body=html,
        subtype=MessageType.html)

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})