from pydantic import BaseModel, ConfigDict, EmailStr
from typing import List

class EmailSchema(BaseModel):
    email: List[EmailStr]

class Pauta(BaseModel):
    tema: str
    descricao: str
    quando: str
    local: str
    responsavel: str
    telefone_responsavel: str
    email_contato: str