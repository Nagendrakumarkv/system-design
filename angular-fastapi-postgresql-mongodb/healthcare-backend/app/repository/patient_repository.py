from app.models.patient_model import Patient

class PatientRepository:

    def create(self, db, patient):
        db_patient = Patient(name=patient.name, age=patient.age)
        db.add(db_patient)
        db.commit()
        db.refresh(db_patient)
        return db_patient

    def get_all(self, db):
        return db.query(Patient).all()