from fastapi import APIRouter
from app.schemas.assessment_schema import AssessmentCreate
from app.services.assessment_service import AssessmentService

router = APIRouter()
service = AssessmentService()

@router.post("/assessments")
def create_assessment(assessment: AssessmentCreate):
    return service.create_assessment(assessment)

@router.get("/assessments/{patient_id}")
def get_assessments(patient_id: int):
    return service.get_assessments(patient_id)