from fastapi import FastAPI
from app.core.database import engine, Base
from app.routes.user import router as user_router
from app.routes.project import router as project_router
from app.routes.task import router as task_router
from app.routes.office import router as office_router
from app.models import user
from app.models import project
from app.models import task
from app.models.office import Office
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(title="DevTrack API")

Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(project_router)
app.include_router(task_router)
app.include_router(office_router)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
] 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")  
def read_root():
    return {"message": "DevTrack API running"}