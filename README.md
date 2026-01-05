# Nourasense

A comprehensive child nutrition and growth assessment tool that provides WHO-standard growth analysis, nutritional recommendations, and developmental milestone tracking for children from birth to 19 years.

## Features

### 🩺 Growth Assessment

- **WHO Standard Z-Scores**: Calculate standardized growth indicators including:
  - Weight-for-age, Height-for-age, BMI-for-age
  - Weight-for-height/length, Head circumference-for-age
  - Arm circumference-for-age
- **Age-Specific Analysis**: Tailored assessments for different developmental stages:
  - Newborns (0-3 months)
  - Infants (3-61 months)
  - Children (61-120 months)
  - Adolescents (120+ months)

### 📊 Diagnostic Classification

- **Automated Diagnosis**: Intelligent classification of growth conditions:
  - Stunting, Wasting, Underweight conditions
  - Microcephaly/Macrocephaly detection
  - Overweight/Obesity assessment
- **Severity Assessment**: Multi-level burden classification system:
  - Normal, Concerning, Critical severity levels
  - Single to Extreme burden categorization

### 🥗 Nutritional Analysis

- **Age-Appropriate Recommendations**: Dietary Reference Intakes (DRI) based on:
  - Vitamins, Minerals, Macronutrients
  - Gender and age-specific requirements
- **Delta Analysis**: Quantifies deviation from optimal measurements

### 📈 Development Tracking

- **Motor Milestone Monitoring**: WHO-based developmental milestones
- **Growth Trajectory Analysis**: Track changes over time

## Installation

```bash
pip install nourasense
```

## Quick Start

```python
from nourasense import Nourasense, ChildData

# Create child data
# NB: While measurements are optional, at least one has to be provided for validation to pass
child_data = ChildData(
    dob="15/06/2020",  # dd/mm/yyyy format
    height=85.5,       # cm (optional)
    weight=12.3,       # kg (optional)
    gender="f",        # 'm' or 'f'
    head_circumference=46.2,  # cm (optional)
    arm_circumference=15.1    # cm (optional)
)

# Initialize assessment
nourasense = Nourasense(child_data)

# Get comprehensive diagnosis
diagnosis, z_scores, deltas = nourasense.diagnose_child(child_data)

print("Growth Assessment:", diagnosis)
print("Z-Scores:", z_scores)
print("Recommendations:", deltas)
```

## API Reference

### Core Classes

#### `ChildData`

Data model for child measurements:

- `dob`: Date of birth (dd/mm/yyyy)
- `height`: Height in centimeters
- `weight`: Weight in kilograms
- `gender`: 'm' for male, 'f' for female
- `head_circumference`: Head circumference in cm (optional)
- `arm_circumference`: Arm circumference in cm (optional)

#### `Nourasense`

Main assessment engine:

- `diagnose_child()`: Returns diagnosis, z-scores, and delta analysis

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
