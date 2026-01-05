from src.nourasense.engine.diagnosis import Diagnosis
from src.nourasense.engine.nutrient_analysis import Nutrition
from src.nourasense.engine.child import Child, ChildData
from src.nourasense.engine.severity import SeverityClassifier, SeverityClass, BurdenClass
from src.nourasense.utils.calculations import calculate_deltas
from pydantic import BaseModel

class DiagnosisResult(BaseModel):
    diagnosis: dict
    z_scores: dict
    deltas: dict
    nutrient_recommendations: dict

class Nourasense:
    def __init__(self, child_data: ChildData):
        self.child_data = child_data
        self.child = Child(child_data)

        
    def modify_keys(self, record):
        record = {k.replace("_", " ").capitalize(): v for k, v in record.items()}
        new_record = {}

        for k, v in record.items():
            if "Bmi" in k:
                new_record["BMI for age"] = v
            else:
                new_record[k] = v

        return new_record   

    def diagnose_child(self, child_measurements):

        diagnosis_model = Diagnosis(
            child= self.child
        )

        diagnosis, z_scores, lms = diagnosis_model.diagnose()

        deltas = calculate_deltas(self.child_data, lms)

        # Modify keys for better readability
        diagnosis = self.modify_keys(diagnosis)
        deltas = self.modify_keys(deltas)

        return diagnosis, z_scores, deltas

