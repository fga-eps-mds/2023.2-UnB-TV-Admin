import pytest
import asyncio
from httpx import AsyncClient
from fastapi.testclient import TestClient
from ..main import app  # Certifique-se de importar o aplicativo FastAPI corretamente

# ...

# Decore a função de teste com pytest.mark.asyncio
@pytest.mark.asyncio
async def test_simple_send():
    # Dados de exemplo com uma lista de endereços de e-mail
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

    # Use o cliente de teste para fazer uma solicitação POST ao endpoint
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/pauta/email", json=test_email_data)

    # Verifique se a resposta possui o código de status esperado (200)
    assert response.status_code == 200
