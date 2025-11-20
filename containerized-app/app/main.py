from fastapi import FastAPI
from auth.routes import router as auth_router
app = FastAPI(title="Containerized Python App")

@app.get("/")
def home():
    return {"message": "FastAPI is protected by WAF"}

@app.get("/hello")
def hello():
    return {"message": "Hello FRom FastAPI"}
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
