from dateutil.relativedelta import relativedelta
from pydantic import BaseModel
import datetime

class ChildData(BaseModel):
    dob: str
    height: float = None
    weight: float = None
    gender: str = None
    head_circumference: float = None
    arm_circumference: float = None

class Child:
    def __init__(self, child_data: ChildData):
        
        self.dob = self.validate_dob(child_data.dob)
        self.height = round(child_data.height, 2) if child_data.height else None
        self.weight = round(child_data.weight, 2) if child_data.weight else None
        self.gender = self.validate_gender(child_data.gender)
        self.head_circumference = round(child_data.head_circumference, 2) if child_data.head_circumference else None
        self.age = self.calculate_age() if self.dob else None
        self.bmi = self.calculate_bmi() if self.height and self.weight else None
        self.arm_circumference = round(child_data.arm_circumference, 2) if child_data.arm_circumference else None
        self.measurement = None
        self.validate_child()
        self.change_in_measurement = {}

    def validate_child(self):
            required_fields = [self.dob, self.gender]
            optional_fields = [self.height, self.weight, self.head_circumference, self.arm_circumference]

            if all(field is not None for field in required_fields):
                if all(field is None for field in optional_fields):
                    raise ValueError('At least one of the optional fields must be provided if required fields are provided.')
                
            if any(field is None for field in required_fields):
                raise ValueError("All of the required fields (dob, gender) must be provided in their corresponding order.")
    

    def validate_dob(self, dob):
        standard = "dd/mm/yyyy"
        if not dob or len(standard.split("/")) != len(dob.split("/")):
            return None
        else:
            return dob

    def validate_gender(self,gender):
        if gender is None or gender.lower() not in ['m', 'f']:
            return None
        else:
            return gender
            
    def calculate_bmi(self):
        if not self.height or not self.weight:
            return
        try:
           bmi =  self.weight / ((self.height * self.height)/10000)

        except ZeroDivisionError:
            return

        return round(bmi, 2)
    
    def calculate_age(self):

        try:

            # Check if the date is in the correct format and meets basic validation
            assert self.dob[0:2].isdigit() and self.dob[3:5].isdigit() and self.dob[6:10].isdigit()

            day = int(self.dob[0:2])
            month = int(self.dob[3:5])
            year = int(self.dob[6:10])

            assert day >= 1 and day <= 31
            assert month >= 1 and month <= 12
            assert year > 1900 and year <= datetime.date.today().year 
            
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

            current_date = datetime.date.today()

            birth_date = datetime.date(year, month, day) 

            age = relativedelta(current_date, birth_date)

            age_in_months = age.years * 12 + age.months + age.days / month_number_to_days[month]
            
            return round(age_in_months, 2)
        
        except AssertionError:
            raise ValueError("Invalid date format. Please use 'dd/mm/yyyy' format.")
