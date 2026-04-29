from app.repository.assessment_repository import AssessmentRepository

class AssessmentService:

    def __init__(self):
        self.repo = AssessmentRepository()

    def create_assessment(self, assessment):
        return {"id": self.repo.create(assessment.dict())}

    def get_assessments(self, patient_id):
        return self.repo.get_by_patient(patient_id)