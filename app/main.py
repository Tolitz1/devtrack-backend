from fastapi import FastAPI
from app.core.database import engine, Base
from app.models import user
from app.routes.user import router as user_router

app = FastAPI(title="DevTrack API")

Base.metadata.create_all(bind=engine)

app.include_router(user_router)

@app.get("/")  
def read_root():
    return {"message": "DevTrack API running"}