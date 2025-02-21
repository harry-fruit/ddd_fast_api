from fastapi import FastAPI
from app.presentation.routes import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def health_check():
    return {"message": "API está rodando!"}