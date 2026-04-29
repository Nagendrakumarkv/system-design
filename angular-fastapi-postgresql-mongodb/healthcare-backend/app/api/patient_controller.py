from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.patient_schema import PatientCreate
from app.services.patient_service import PatientService
from app.core.database import SessionLocal

router = APIRouter()
service = PatientService()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/patients")
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    return service.create_patient(db, patient)

@router.get("/patients")
def get_patients(db: Session = Depends(get_db)):
    return service.get_patients(db)