from fastapi.testclient import TestClient 
from unittest.mock import patch
from main import app 

client = TestClient(app)

#teste da rota /health
def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "mode": "mock"}

#teste com imagem valida
def test_analyze_imagem_valida():
    with patch('main.random.choice', return_value=True), \
            patch('main.random.uniform', return_value=0.87):
        
        image_fake = b"fake image content"
        response = client.post(
            "/analyze", 
            files={"file": ("foto.jpg", image_fake, "image/jpeg")}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["filename"] == "foto.jpg"
        assert data["is_ai_generated"] == True
        assert data["confidence"] == 0.87
        assert data["label"] == "AI-generated"

#teste com foce_result=ai
def test_analyze_force_ai():
    image_fake = b'fake image content'
    response = client.post(
        "/analyze?force_result=ai",
        files={"file": ("foto.jpg", image_fake, "image/jpeg")}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["is_ai_generated"] == True
    assert data["confidence"] == 0.94
    assert data["label"] == "AI-generated"

#teste com force_result=real
def test_analyze_force_real():
    image_fake = b'fake image content'
    response = client.post(
        "/analyze?force_result=real",
        files={"file": ("foto.jpg", image_fake, "image/jpeg")}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["is_ai_generated"] == False
    assert data["confidence"] == 0.91
    assert data["label"] == "Real"

#teste com arquivo invalido
def test_analyze_arquivo_invalido():
    arquivo_fake = b'conteudo qualquer'
    response = client.post(
        "/analyze",
        files={"file": ("documento.pdf", arquivo_fake, "application/pdf")}
    )
    assert response.status_code == 400
    assert "Tipo nao suportado" in response.json()["detail"]

#teste com arquivo muito grande
def test_analyze_arquivo_grande():
    arquivo_grande = b'x' * (6 * 1024 * 1024)  # 1 MB
    response = client.post(
        "/analyze",
        files={"file": ("foto.jpg", arquivo_grande, "image/jpeg")}
    )
    assert response.status_code == 400
    assert "Arquivo muito grande" in response.json()["detail"]