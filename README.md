# Nourasense

A comprehensive child nutrition and growth assessment tool that provides WHO-standard growth analysis, nutritional recommendations, and developmental milestone tracking for children from birth to 19 years.

## Features

### Growth Assessment

- **WHO Standard Z-Scores**: Calculate standardized growth indicators including:
  - Weight-for-age, Height-for-age, BMI-for-age
  - Weight-for-height/length, Head circumference-for-age
  - Arm circumference-for-age
- **Age-Specific Analysis**: Tailored assessments for different developmental stages:
  - Newborns (0-3 months)
  - Infants (3-61 months)
  - Children (61-120 months)
  - Adolescents (120+ months)

### Diagnostic Classification

- **Automated Diagnosis**: Intelligent classification of growth conditions:
  - Stunting, Wasting, Underweight conditions
  - Microcephaly/Macrocephaly detection
  - Overweight/Obesity assessment
- **Severity Assessment**: Multi-level burden classification system:
  - Normal, Concerning, Critical severity levels
  - Single to Extreme burden categorization

### Nutritional Analysis

- **Age-Appropriate Recommendations**: Dietary Reference Intakes (DRI) based on:
  - Vitamins, Minerals, Macronutrients
  - Gender and age-specific requirements
- **Delta Analysis**: Quantifies deviation from optimal measurements

### Development Tracking

- **Motor Milestone Monitoring**: WHO-based developmental milestones
- **Growth Trajectory Analysis**: Track changes over time

## Quick Start

The code shown below

```python
from nourasense import Nourasense, ChildData, DiagnosisResult

# Create child data
# NB: While measurements are optional, at least one has to be provided for validation to pass
child_data = ChildData(
    dob="25/11/2022", # dd/mm/yyyy format
    height=65.0,      # cm (optional)
    weight=7.5,       # kg (optional)
    gender="m",       # 'm' or 'f'
    arm_circumference=15.0,   # cm (optional)
    head_circumference=40.0,  # cm (optional)
)

# Initialize assessment
nourasense = Nourasense(child_data)

# Generate comprehensive diagnosis results
diagnosis_result: DiagnosisResult = nourasense.diagnose_child()

print(f"Diagnosis:\n{diagnosis_result.diagnosis}\n")
print(f"Z-scores:\n{diagnosis_result.z_scores}\n")
print(f"Deltas:\n{diagnosis_result.deltas}\n")
print(f"Nutrient Recommendations:\n{diagnosis_result.nutrient_recommendations}\n")
print(f"Severity Classification:\n{diagnosis_result.severity_classification}\n")
print(f"Burden Classification:\n{diagnosis_result.burden_classification}\n")
```

## API Reference

### Core Classes and Data Objects

#### `ChildData`

Data model for child measurements:

- `dob`: Date of birth (dd/mm/yyyy)
- `height`: Height in centimeters
- `weight`: Weight in kilograms
- `gender`: 'm' for male, 'f' for female
- `head_circumference`: Head circumference in cm (optional)
- `arm_circumference`: Arm circumference in cm (optional)

#### `Child`

Encapsulates child data and age calculations, and represents a child:

- `dob`: Validated date of birth string (dd/mm/yyyy format)
- `height`: Height in cm (rounded to 2 decimal places)
- `weight`: Weight in kg (rounded to 2 decimal places)
- `gender`: Validated gender ('m' or 'f')
- `head_circumference`: Head circumference in cm (optional)
- `arm_circumference`: Arm circumference in cm (optional)
- `age`: Age in months (calculated from DOB)
- `bmi`: Body Mass Index (calculated from height/weight)
- `measurement`: Placeholder for measurement data
- `change_in_measurement`: Dictionary for tracking measurement changes
- `validate_child()`: Ensures required fields (dob, gender) and at least one measurement are provided
- `validate_dob()`: Validates date of birth format
- `validate_gender()`: Validates gender input
- `calculate_age()`: Computes precise age in months from date of birth
- `calculate_bmi()`: Computes BMI from height and weight measurements

#### `DiagnosisResult`

Holds the result of a diagnosis and contains the following information:

- `diagnosis`: Dictionary of growth condition classifications (e.g., stunting, wasting, underweight)
- `z_scores`: Dictionary of standardized z-scores for each growth indicator
- `deltas`: Dictionary of deviations from optimal measurements with descriptive explanations
- `nutrient_recommendations`: Dictionary of age-appropriate dietary reference intakes (vitamins, minerals, macronutrients)
- `severity_classification`: Dictionary mapping each indicator to severity level (Normal, Concerning, Critical)
- `burden_classification`: Overall malnutrition burden category (No Burden to Extreme Burden)

#### `Nourasense`

Main assessment engine:

- `diagnose_child()`: Returns a `Diagnosis Result` object

#### `SeverityClassifier`

Burden and severity assessment:

- `classify_burden()`: Categorizes overall malnutrition burden
- `classify_severity()`: Assesses individual indicator severity

#### `Nutrition`

Nutritional recommendations:

- `get_recommendations()`: Returns age-appropriate DRI values

## Growth Standards

Nourasense uses WHO Child Growth Standards and references:

- WHO Growth Charts (0-5 years)
- WHO Reference Charts (5-19 years)
- Motor Development Milestones
- Dietary Reference Intakes (DRI)

## Age Groups & Indicators

| Age Range     | Available Indicators                 |
| ------------- | ------------------------------------ |
| 0-3 months    | WFA, HFA, HCFA, BMIFA                |
| 3-61 months   | WFA, HFA, HCFA, BMIFA, WFH/WFL, ACFA |
| 61-120 months | WFA, HFA, BMIFA, WFH                 |
| 120+ months   | HFA, BMIFA, ACFA                     |

**Legend**: WFA (Weight-for-Age), HFA (Height-for-Age), HCFA (Head Circumference-for-Age), BMIFA (BMI-for-Age), WFH/WFL (Weight-for-Height/Length), ACFA (Arm Circumference-for-Age)

## Requirements

- Python ≥ 3.12
- pydantic ≥ 2.12.5
- python-dateutil ≥ 2.9.0

## License

This project uses WHO growth standards and references. Please ensure compliance with WHO data usage policies.

## Contributing

Contributions are welcome! Please ensure all growth calculations follow WHO standards.

## Author

**Vinlaw Mudehwe** - [me@vinlawmudehwe.com](mailto:me@vinlawmudehwe.com)

For more updates on stuff I am working on, check out my website at [vinlawmudehwe.com](https://vinlawmudehwe.com)
