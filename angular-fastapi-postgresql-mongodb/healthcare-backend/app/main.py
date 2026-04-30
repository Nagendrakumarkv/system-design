from fastapi import FastAPI
from app.api.patient_controller import router
from app.api.assessment_controller import router as assessment_router
from app.api.auth_controller import router as auth_router
from app.core.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)
app.include_router(assessment_router)
app.include_router(auth_router)