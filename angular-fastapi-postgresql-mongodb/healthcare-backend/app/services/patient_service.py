from app.repository.patient_repository import PatientRepository

class PatientService:

    def __init__(self):
        self.repo = PatientRepository()

    def create_patient(self, db, patient):
        if patient.age < 0:
            raise Exception("Invalid age")
        return self.repo.create(db, patient)

    def get_patients(self, db):
        return self.repo.get_all(db)