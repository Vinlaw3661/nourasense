from src.nourasense.nourasense import Nourasense, ChildData, DiagnosisResult

child_data = ChildData(
    dob="25/11/2022",
    height=65.0,
    weight=7.5,
    gender="m",
    arm_circumference=15.0,
    head_circumference=40.0,
)

nourasense = Nourasense(child_data)

diagnosis_result: DiagnosisResult = nourasense.diagnose_child()

print(f"Diagnosis:\n{diagnosis_result.diagnosis}\n")
print(f"Z-scores:\n{diagnosis_result.z_scores}\n")
print(f"Deltas:\n{diagnosis_result.deltas}\n")
print(f"Nutrient Recommendations:\n{diagnosis_result.nutrient_recommendations}\n")
print(f"Severity Classification:\n{diagnosis_result.severity_classification}\n")
print(f"Burden Classification:\n{diagnosis_result.burden_classification}\n")