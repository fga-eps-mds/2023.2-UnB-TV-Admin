import pytest
import asyncio
from httpx import AsyncClient
from fastapi.testclient import TestClient
from src.main import app  

client = TestClient(app)

@pytest.mark.asyncio
async def test_simple_send():
    
    test_email_data = {
        "recipients": ["ricardoloureiro75@gmail.com"],
        "tema": "Exemplo de Tema",
        "descricao": "Exemplo de Descrição",
        "quando": "Exemplo de Quando",
        "local": "Exemplo de Local",
        "responsavel": "Exemplo de Responsável",
        "telefone_responsavel": "Exemplo de Telefone",
        "email_contato": "geraldovictor@outlook.com"
    }

    
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/pauta/email", json=test_email_data)

    
    assert response.status_code == 200

def test_root_request():
  response = client.get('/')
  data = response.json()
  assert response.status_code == 200
  assert data['message'] == 'UnB-TV!'