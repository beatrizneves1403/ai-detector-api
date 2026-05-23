 # AI Detector API

 API REST para detecção de imagens geradas por Inteligência Artificial. Desenvolvida com FastAPI. 

> Esta é a versão mock da API - os resultados são simulados.
> O modelo de IA real será integrado futuramente. 

## Tecnologias
- Python 3.14
- FastAPI
- Uvicorn 
- Pydantic 

## Como rodar localmente
### Pré-requisitos
- Python 3.10 ou superior
### Instalação
1. Clone o repositório
```
git clone https://github.com/seu-usuario/ai-detector-api.git
cd ai-detector-api
```

2. Crie e ative o ambiente virtual
```
python -m venv venv
venv\Scripts\activate
```
3. Instale as dependências 
```
pip install -r requirements.txt
```
4. Rode a API
```
uvicorn main:app --reload
```
5. Acesse a documentação
```
http://127.0.0.1:8000/docs
```

## Endpoints

### GET /health
Verifica se a API está no ar. 

**Resposta:**
```json
{
    "status": "ok",
    "mode": "mock"
}
```

### POST /analyze
Recebe uma imagem e retorna se foi gerada por IA. 

**Parâmetros:**
- `file` - imagem nos formatos PNG, JPG ou WEBP (máximo 5MB)
- `force_result`- opcional. Use `ai` ou `real` para forçar um resultado nos testes

**Resposta:**
```json
{
    "filename": "foto.jpg",
    "is_ai_generated": true,
    "confidence": 0.87,
    "label": "AI-generated"
}
```

**Erros:**
-`400` - tipo de arquivo não suportado
-`400` - arquivo maior que 5MB

## Próximos passos
- [ ] Integrar modelo de IA real de detecção
- [ ] Adicionar suporte a URL de imagem 
- [ ] Criar interface web para upload 
- [ ] Adicionar testes automatizados

## Autor

Feito por Beatriz Neves (https://github.com/beatrizneves1403)