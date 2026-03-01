from fastapi import FastAPI
from app.core.database import engine, Base
from app.models import user
from app.routes.user import router as user_router
from app.routes.project import router as project_router
from app.models import project


app = FastAPI(title="DevTrack API")

Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(project_router)

@app.get("/")  
def read_root():
    return {"message": "DevTrack API running"}