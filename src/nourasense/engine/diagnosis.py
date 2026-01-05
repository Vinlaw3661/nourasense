from decimal import Decimal
from src.pygrowup.pygrowup import Observation

class Diagnosis:

    def __init__(self, child):
        self.child = child

    def diagnose(self):
        sex = Observation.MALE if self.child.gender == 'm' else Observation.FEMALE
        age_in_months = self.child.age

        if age_in_months <= 0 or age_in_months > 228:
            raise ValueError("Child's date of birth cannot be the same as the date of diagnosis")

        obs = Observation(sex=sex, age_in_months=age_in_months)
        lms = {}
        diagnosis = {}
        z_scores = {}

        return self.compute_indicators(obs, diagnosis, z_scores, lms)

    def compute_indicators(self, obs, diagnosis, z_scores, lms):
        child = self.child
        age = child.age

        def update_result(name, z, lms_val):
            if z is not None and lms_val is not None:
                z_scores[name] = z
                lms[name] = lms_val
                diagnosis[name] = assign_diagnosis(name, z)

        # Newborns (age <= 3 months)
        if age <= 3:
            if child.weight is not None and age <= 120:
                z, l = get_z_and_lms(obs, "wfa","weight", child.weight)
                update_result("weight_for_age", z, l)
            if child.height is not None:
                z, l = get_height_for_age(obs, child.height)
                update_result("height_for_age", z, l)
            if child.head_circumference is not None:
                z, l = get_z_and_lms(obs, "hcfa","head_circumference", child.head_circumference)
                update_result("head_circumference_for_age", z, l)
            if child.bmi is not None:
                z, l = get_bmi_z_and_lms(obs, child.bmi)
                update_result("bmi_for_age", z, l)

        # Infants (3 < age < 61 months)
        elif 3 < age < 61:
            if child.weight is not None and age <= 120:
                z, l = get_z_and_lms(obs, "wfa","weight", child.weight)
                update_result("weight_for_age", z, l)
            if child.height is not None:
                z, l = get_height_for_age(obs, child.height)
                update_result("height_for_age", z, l)
            if child.head_circumference is not None:
                z, l = get_z_and_lms(obs, "hcfa","head_circumference", child.head_circumference)
                update_result("head_circumference_for_age", z, l)
            if child.bmi is not None:
                z, l = get_bmi_z_and_lms(obs, child.bmi)
                update_result("bmi_for_age", z, l)
            if child.height is not None and child.weight is not None:
                z, l = get_wfl_or_wfh(obs, "wfl", child.weight, child.height)
                update_result("weight_for_height", z, l)
            if child.arm_circumference is not None:
                z, l = get_z_and_lms(obs, "acfa","arm_circumference", child.arm_circumference)
                update_result("arm_circumference_for_age", z, l)

        # Children (61 <= age <= 120 months)
        elif 61 <= age <= 120:
            if child.weight is not None and age <= 120:
                z, l = get_z_and_lms(obs, "wfa","weight", child.weight)
                update_result("weight_for_age", z, l)
            if child.height is not None:
                z, l = get_height_for_age(obs, child.height)
                update_result("height_for_age", z, l)
            if child.bmi is not None:
                z, l = get_bmi_z_and_lms(obs, child.bmi)
                update_result("bmi_for_age", z, l)
            if child.height is not None and child.weight is not None:
                z, l = get_wfl_or_wfh(obs, "wfh", child.weight, child.height)
                update_result("weight_for_height", z, l)

        # Adolescents (age > 120 months)
        elif age > 120:
            if child.height is not None:
                z, l = get_height_for_age(obs, child.height)
                update_result("height_for_age", z, l)
            if child.bmi is not None:
                z, l = get_bmi_z_and_lms(obs, child.bmi)
                update_result("bmi_for_age", z, l)
            if child.arm_circumference is not None:
                z, l = get_z_and_lms(obs, "acfa","arm_circumference", child.arm_circumference)
                update_result("arm_circumference_for_age", z, l)

        return diagnosis, z_scores, lms


def get_z_and_lms(obs, code, table, value):
    z = float(getattr(obs, f"{table}_for_age")(Decimal(str(value))))
    lms = obs._get_box_cox_variables(code, obs.sex, obs.t)
    return z, lms


def get_height_for_age(obs, height):
    z = float(obs.length_or_height_for_age(Decimal(str(height))))
    lms = obs._get_box_cox_variables("lfa", obs.sex, obs.t)
    return z, lms


def get_bmi_z_and_lms(obs, bmi):
    if bmi is not None and 5 <= bmi <= 60:
        z = float(obs.bmi_for_age(Decimal(str(bmi))))
        lms = obs._get_box_cox_variables("bmifa", obs.sex, obs.t)
        return z, lms
    return None, None


def get_wfl_or_wfh(obs, kind, weight, height):
    if kind == "wfl" and height is not None and 45 <= height <= 110:
        z = float(obs.weight_for_length(Decimal(str(weight)), Decimal(str(height))))
        lms = obs._get_box_cox_variables("wfl", obs.sex, height)
        return z, lms
    elif kind == "wfh" and height is not None and 65 <= height <= 120:
        z = float(obs.weight_for_height(Decimal(str(weight)), Decimal(str(height))))
        lms = obs._get_box_cox_variables("wfh", obs.sex, height)
        return z, lms
    return None, None


def assign_diagnosis(name, z):
    if z is None:
        return None

    if name == "head_circumference_for_age":
        if z < -3:
            return 'Severe Microcephaly'
        elif z < -2:
            return 'Microcephaly'
        elif z < 2:
            return 'Normal'
        elif z < 3:
            return 'Macrocephaly'
        else:
            return 'Severe Macrocephaly'

    elif name == "weight_for_age":
        if z < -3:
            return 'Severe Underweight'
        elif z < -2:
            return 'Underweight'
        elif z < 1:
            return 'Normal'
        else:
            return 'Possible risk of growth problem'

    elif name == "height_for_age":
        if z < -3:
            return 'Severe Stunting'
        elif z < -2:
            return 'Stunting'
        elif z < 3:
            return 'Normal'
        else:
            return 'Normal (May indicate endocrine disorder)'

    elif name == "bmi_for_age":
        if z < -3:
            return 'Severe Underweight'
        elif z < -2:
            return 'Underweight'
        elif z < 1:
            return 'Normal'
        elif z < 2:
            return 'Possible risk of overweight'
        elif z < 3:
            return 'Overweight'
        else:
            return 'Obese'

    elif name in ("weight_for_height", "weight_for_length"):
        if z < -3:
            return 'Severe Wasting'
        elif z < -2:
            return 'Wasting'
        elif z < 2:
            return 'Normal'
        elif z < 3:
            return 'Overweight'
        else:
            return 'Obese'

    elif name == "arm_circumference_for_age":
        if z < -3:
            return 'Severe depletion of muscle and fat stores'
        elif z < -2:
            return 'Moderate depletion of muscle and fat stores'
        elif z < 2:
            return 'Normal body composition'
        elif z < 3:
            return 'Elevated fat or muscle mass'
        else:
            return 'Excessive fat or muscle mass'
