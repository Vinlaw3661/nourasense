from src.nourasense.data.dri_tables import VITAMINS, MINERALS, MACRONUTRIENTS
from src.nourasense.engine.child import Child

VITAMINS_TABLE = VITAMINS
MINERALS_TABLE = MINERALS
MACRONUTRIENTS_TABLE = MACRONUTRIENTS

def get_age_group(age,gender):

    try:
        assert gender in ['m','f'], "Gender must be 'm' or 'f'"

        age_years = int(age//12)
        groups = {}
        if age >= 0 and age <= 12:
            groups['age_group'] = 'Infants'
            if age <= 6:
                groups['nutrient_group'] = '0-6 mo'
                return groups
            else:
                groups['nutrient_group'] = '7-12 mo'
                return groups
        
        elif age_years >= 1 and age_years <= 8:
            groups['age_group'] = 'Children'
            
            if age_years >= 1 and age_years <= 3:
                groups['nutrient_group'] = '1-3 y'
                return groups
            else:
                groups['nutrient_group'] = '4-8 y'
                return groups
            
        elif age_years >= 9 and age_years <= 19:
            groups['age_group'] = 'Males' if gender == 'm' else 'Females'

            if age_years >= 9 and age_years <= 13:
                groups['nutrient_group'] = '9-13 y'
                return groups
            elif age_years >= 14 and age_years <= 18:
                groups['nutrient_group'] = '14-18 y'
                return groups
            else:
                groups['nutrient_group'] = '19-30 y'
                return groups
                
    except AssertionError as e:
        raise ValueError("Gender must be 'm' or 'f'") from e
        
class Nutrition:
    def __init__(self, child: Child):
        self.child_age = child.age
        self.child_gender = child.gender
        self.recommendations = {}

    def get_recommendations(self):
        groups = get_age_group(self.child_age,self.child_gender)
        age_group = groups['age_group']
        nutrient_group = groups['nutrient_group']
        vitamins = VITAMINS_TABLE[age_group][nutrient_group]
        minerals = MINERALS_TABLE[age_group][nutrient_group]
        macronutrients = MACRONUTRIENTS_TABLE[age_group][nutrient_group]
        self.recommendations['vitamins'] = vitamins
        self.recommendations['minerals'] = minerals
        self.recommendations['macronutrients'] = macronutrients

        return self.recommendations
    
