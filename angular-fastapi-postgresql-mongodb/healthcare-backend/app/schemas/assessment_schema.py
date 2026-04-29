from pydantic import BaseModel
from typing import List, Dict

class AssessmentCreate(BaseModel):
    patientId: int
    questions: List[Dict]