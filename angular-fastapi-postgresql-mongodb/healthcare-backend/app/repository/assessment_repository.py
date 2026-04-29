from app.core.mongodb import assessment_collection

class AssessmentRepository:

    def create(self, assessment):
        result = assessment_collection.insert_one(assessment)
        return str(result.inserted_id)   # ✅ convert ObjectId to string

    def get_by_patient(self, patient_id):
        data = list(assessment_collection.find({"patientId": patient_id}))
        
        # ✅ Convert ObjectId to string
        for item in data:
            item["_id"] = str(item["_id"])
        
        return data