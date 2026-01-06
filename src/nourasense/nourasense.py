from src.nourasense.engine.diagnosis import *
from src.nourasense.engine.nutrient_analysis import *
from src.nourasense.engine.child import *
from src.nourasense.engine.severity import *
from src.nourasense.utils.calculations import *
from src.nourasense.data.dri_tables import *
from src.nourasense.data.milestone_tables import *
from pydantic import BaseModel

class DiagnosisResult(BaseModel):
    diagnosis: dict
    z_scores: dict
    deltas: dict
    nutrient_recommendations: dict
    severity_classification: dict 
    burden_classification: str

class Nourasense:
    def __init__(self, child_data: ChildData):
        self.child_data = child_data
        self.child = Child(child_data)
        self.diagnosis_model = Diagnosis(child=self.child)
        self.nutrition_model = Nutrition(child=self.child)
        
    def modify_keys(self, record: dict) -> dict:
        record = {k.replace("_", " ").capitalize(): v for k, v in record.items()}
        new_record = {}

        for k, v in record.items():
            if "Bmi" in k:
                new_record["BMI for age"] = v
            else:
                new_record[k] = v

        return new_record   

    def diagnose_child(self) -> DiagnosisResult:

        diagnosis, z_scores, lms = self.diagnosis_model.diagnose()

        deltas = calculate_deltas(self.child, lms)

        nutrient_recommendations = self.nutrition_model.get_recommendations() 

        severity_classifier = SeverityClassifier(z_scores=z_scores)
        severity_classification = severity_classifier.classify_severity()
        burden_classification = severity_classifier.classify_burden()  

        # Modify keys for better readability
        diagnosis = self.modify_keys(diagnosis)
        deltas = self.modify_keys(deltas)
        z_scores = self.modify_keys(z_scores)

        return DiagnosisResult(
            diagnosis=diagnosis,
            z_scores=z_scores,
            deltas=deltas,
            nutrient_recommendations=nutrient_recommendations,
            severity_classification=severity_classification,
            burden_classification=burden_classification
        )
