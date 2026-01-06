from src.nourasense.engine.child import Child
from datetime import datetime
from dateutil.relativedelta import relativedelta
import math

def calculate_age(dob_str: str) -> float:

    try:

        # Check if the date is in the correct format and meets basic validation
        assert dob_str[0:2].isdigit() and dob_str[3:5].isdigit() and dob_str[6:10].isdigit()

        day = int(dob_str[0:2])
        month = int(dob_str[3:5])
        year = int(dob_str[6:10])
        assert day >= 1 and day <= 31
        assert month >= 1 and month <= 12
        assert year > 1900 and year <= datetime.today().year 
        
        # Convert input to integer and separate day, month and year
        # Calculate the age in months
        month_number_to_days ={
            1: 31,
            2: 28 if year % 4 != 0 else 29,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }

        current_date = datetime.today()

        birth_date = datetime.date(year, month, day) 

        age = relativedelta(current_date, birth_date)

        age_in_months = age.years * 12 + age.months + age.days / month_number_to_days[month]
        
        return round(age_in_months, 2)
    
    except AssertionError:
        raise ValueError("Invalid date format. Please use 'dd/mm/yyyy' format.")
    
def calculate_bmi(weight, height):
    bmi =  weight / ((height * height)/10000)
    return round(bmi, 2)


def calculate_measurement(L, M, S, Z):
    L, M, S, Z = float(L), float(M), float(S), float(Z)

    if L != 0:
        X = M * (1 + L * S * Z) ** (1 / L)
    else:
        X = M * math.exp(S * Z)

    return X

def calculate_deltas(child: Child, lms):
    
    deltas = {}

    for key in lms:
        L, M, S = lms[key]["l"], lms[key]["m"], lms[key]["s"]

        optimal = calculate_measurement(L, M, S, Z=0)

        if key == "weight_for_height" or key == "weight_for_age":
            current = child.weight
        
        elif key == "height_for_age":
            current = child.height

        elif key == "head_circumference_for_age":
            current = child.head_circumference

        elif key == "bmi_for_age":
            current = child.bmi

        delta = current - optimal

        if abs(delta) < 1e-3:
            continue  # Value is close enough to optimal

        direction = "above" if delta > 0 else "below"
        delta_val = abs(delta)

        if key == "weight_for_height":
            deltas[key] = f"The child's weight is {delta_val:.2f} kg {direction} the optimal weight for height."
        elif key == "height_for_age":
            deltas[key] = f"The child's height is {delta_val:.2f} cm {direction} the optimal height for age."
        elif key == "weight_for_age":
            deltas[key] = f"The child's weight is {delta_val:.2f} kg {direction} the optimal weight for age."
        elif key == "head_circumference_for_age":
            deltas[key] = f"The child's head circumference is {delta_val:.2f} cm {direction} the optimal head circumference for age."
        elif key == "bmi_for_age":
            deltas[key] = f"The child's BMI is {delta_val:.2f} kg/m² {direction} the optimal BMI for age."
        else:
            deltas[key] = f"The child's {key.replace('_', ' ')} is {delta_val:.2f} units {direction} the optimal value."
    
    return deltas