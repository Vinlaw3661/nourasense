from src.nourasense.engine.diagnosis import Diagnosis
from src.nourasense.engine.child import Child

def modify_keys(record):
    record = {k.replace("_", " ").capitalize(): v for k, v in record.items()}
    new_record = {}

    for k, v in record.items():
        if "Bmi" in k:
            new_record["BMI for age"] = v
        else:
            new_record[k] = v

    return new_record   

def diagnose_child(child_measurements):

    child = Child(
        dob = child_measurements["dob"],
        height = child_measurements["height"],
        weight= child_measurements["weight"],
        head_circumference= child_measurements["head_circumference"],
        gender= child_measurements["sex"]
    )

    diagnosis_model = Diagnosis(
        child= child
    )

    child_measurements["bmi"] = child.bmi

    diagnosis, z_scores, lms = diagnosis_model.diagnose()

    deltas = calculate_deltas(child_measurements, lms)

    # Modify keys for better readability
    diagnosis = modify_keys(diagnosis)
    deltas = modify_keys(deltas)

    return diagnosis, z_scores, deltas

