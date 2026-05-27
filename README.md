
# AI Education Support Chatbot

## Tech Stack
- FastAPI
- Streamlit
- LangChain
- FAISS
- OpenAI / Ollama

## Run Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Run Frontend
```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

## Docker
```bash
docker-compose up --build
```
