# This data is based on information extracted from the Dietary Reference Intakes (DRIs) provided by the USDA.
MACRONUTRIENTS =  {
    "Infants": {
        "0-6 mo": {"Total Water (L/d)": 0.7, "Carbohydrate (g/d)": 60, "Total Fiber (g/d)": 0.0,
                   "Fat (g/d)": 31, "Linoleic Acid (g/d)": 4.4, "α-Linolenic Acid (g/d)": 0.5, "Protein (g/d)": 9.1},
        "7-12 mo": {"Total Water (L/d)": 0.8, "Carbohydrate (g/d)": 95, "Total Fiber (g/d)": 0.0,
                    "Fat (g/d)": 30, "Linoleic Acid (g/d)": 4.6, "α-Linolenic Acid (g/d)": 0.5, "Protein (g/d)": 11.0}
    },
    "Children": {
        "1-3 y": {"Total Water (L/d)": 1.3, "Carbohydrate (g/d)": 130, "Total Fiber (g/d)": 19,
                  "Fat (g/d)": 0.0, "Linoleic Acid (g/d)": 7, "α-Linolenic Acid (g/d)": 0.7, "Protein (g/d)": 13},
        "4-8 y": {"Total Water (L/d)": 1.7, "Carbohydrate (g/d)": 130, "Total Fiber (g/d)": 25,
                  "Fat (g/d)": 0.0, "Linoleic Acid (g/d)": 10, "α-Linolenic Acid (g/d)": 0.9, "Protein (g/d)": 19}
    },
    "Males": {
        "9-13 y": {"Total Water (L/d)": 2.4, "Carbohydrate (g/d)": 130, "Total Fiber (g/d)": 31,
                   "Fat (g/d)": 0.0, "Linoleic Acid (g/d)": 12, "α-Linolenic Acid (g/d)": 1.2, "Protein (g/d)": 34},
        "14-18 y": {"Total Water (L/d)": 3.3, "Carbohydrate (g/d)": 130, "Total Fiber (g/d)": 38,
                    "Fat (g/d)": 0.0, "Linoleic Acid (g/d)": 16, "α-Linolenic Acid (g/d)": 1.6, "Protein (g/d)": 52},
        "19-30 y": {"Total Water (L/d)": 3.7, "Carbohydrate (g/d)": 130, "Total Fiber (g/d)": 38,
                    "Fat (g/d)": 0.0, "Linoleic Acid (g/d)": 17, "α-Linolenic Acid (g/d)": 1.6, "Protein (g/d)": 56},
        "31-50 y": {"Total Water (L/d)": 3.7, "Carbohydrate (g/d)": 130, "Total Fiber (g/d)": 38,
                    "Fat (g/d)": 0.0, "Linoleic Acid (g/d)": 17, "α-Linolenic Acid (g/d)": 1.6, "Protein (g/d)": 56},
        "51-70 y": {"Total Water (L/d)": 3.7, "Carbohydrate (g/d)": 130, "Total Fiber (g/d)": 30,
                    "Fat (g/d)": 0.0, "Linoleic Acid (g/d)": 14, "α-Linolenic Acid (g/d)": 1.6, "Protein (g/d)": 56},
        "> 70 y": {"Total Water (L/d)": 3.7, "Carbohydrate (g/d)": 130, "Total Fiber (g/d)": 30,
                   "Fat (g/d)": 0.0, "Linoleic Acid (g/d)": 14, "α-Linolenic Acid (g/d)": 1.6, "Protein (g/d)": 56}
    },
    "Females": {
        "9-13 y": {"Total Water (L/d)": 2.1, "Carbohydrate (g/d)": 130, "Total Fiber (g/d)": 26,
                   "Fat (g/d)": 0.0, "Linoleic Acid (g/d)": 10, "α-Linolenic Acid (g/d)": 1.0, "Protein (g/d)": 34},
        "14-18 y": {"Total Water (L/d)": 2.3, "Carbohydrate (g/d)": 130, "Total Fiber (g/d)": 26,
                    "Fat (g/d)": 0.0, "Linoleic Acid (g/d)": 11, "α-Linolenic Acid (g/d)": 1.1, "Protein (g/d)": 46},
        "19-30 y": {"Total Water (L/d)": 2.7, "Carbohydrate (g/d)": 130, "Total Fiber (g/d)": 25,
                    "Fat (g/d)": 0.0, "Linoleic Acid (g/d)": 12, "α-Linolenic Acid (g/d)": 1.1, "Protein (g/d)": 46},
        "31-50 y": {"Total Water (L/d)": 2.7, "Carbohydrate (g/d)": 130, "Total Fiber (g/d)": 25,
                    "Fat (g/d)": 0.0, "Linoleic Acid (g/d)": 12, "α-Linolenic Acid (g/d)": 1.1, "Protein (g/d)": 46},
        "51-70 y": {"Total Water (L/d)": 2.7, "Carbohydrate (g/d)": 130, "Total Fiber (g/d)": 21,
                    "Fat (g/d)": 0.0, "Linoleic Acid (g/d)": 11, "α-Linolenic Acid (g/d)": 1.1, "Protein (g/d)": 46},
        "> 70 y": {"Total Water (L/d)": 2.7, "Carbohydrate (g/d)": 130, "Total Fiber (g/d)": 21,
                   "Fat (g/d)": 0.0, "Linoleic Acid (g/d)": 11, "α-Linolenic Acid (g/d)": 1.1, "Protein (g/d)": 46}
    }
}

VITAMINS = {
    "Infants": {
        "0-6 mo": {"Vitamin A (µg/d)": 400, "Vitamin C (mg/d)": 40, "Vitamin D (µg/d)": 10, "Vitamin E (mg/d)": 4,
                   "Vitamin K (µg/d)": 2.0, "Thiamin (mg/d)": 0.2, "Riboflavin (mg/d)": 0.3, "Niacin (mg/d)": 2,
                   "Vitamin B6 (mg/d)": 0.1, "Folate (µg/d)": 65, "Vitamin B12 (µg/d)": 0.4, 
                   "Pantothenic Acid (mg/d)": 1.7, "Biotin (µg/d)": 5, "Choline (mg/d)": 125},
        "7-12 mo": {"Vitamin A (µg/d)": 500, "Vitamin C (mg/d)": 50, "Vitamin D (µg/d)": 10, "Vitamin E (mg/d)": 5,
                    "Vitamin K (µg/d)": 2.5, "Thiamin (mg/d)": 0.3, "Riboflavin (mg/d)": 0.4, "Niacin (mg/d)": 4,
                    "Vitamin B6 (mg/d)": 0.3, "Folate (µg/d)": 80, "Vitamin B12 (µg/d)": 0.5,
                    "Pantothenic Acid (mg/d)": 1.8, "Biotin (µg/d)": 6, "Choline (mg/d)": 150}
    },
    "Children": {
        "1-3 y": {"Vitamin A (µg/d)": 300, "Vitamin C (mg/d)": 15, "Vitamin D (µg/d)": 15, "Vitamin E (mg/d)": 6,
                  "Vitamin K (µg/d)": 30, "Thiamin (mg/d)": 0.5, "Riboflavin (mg/d)": 0.5, "Niacin (mg/d)": 6,
                  "Vitamin B6 (mg/d)": 0.5, "Folate (µg/d)": 150, "Vitamin B12 (µg/d)": 0.9,
                  "Pantothenic Acid (mg/d)": 2, "Biotin (µg/d)": 8, "Choline (mg/d)": 200},
        "4-8 y": {"Vitamin A (µg/d)": 400, "Vitamin C (mg/d)": 25, "Vitamin D (µg/d)": 15, "Vitamin E (mg/d)": 7,
                  "Vitamin K (µg/d)": 55, "Thiamin (mg/d)": 0.6, "Riboflavin (mg/d)": 0.6, "Niacin (mg/d)": 8,
                  "Vitamin B6 (mg/d)": 0.6, "Folate (µg/d)": 200, "Vitamin B12 (µg/d)": 1.2,
                  "Pantothenic Acid (mg/d)": 3, "Biotin (µg/d)": 12, "Choline (mg/d)": 250}
    },
    "Males": {
        "9-13 y": {
            "Vitamin A (µg/d)": 600, "Vitamin C (mg/d)": 45, "Vitamin D (µg/d)": 15, "Vitamin E (mg/d)": 11,
            "Vitamin K (µg/d)": 60, "Thiamin (mg/d)": 0.9, "Riboflavin (mg/d)": 0.9, "Niacin (mg/d)": 12,
            "Vitamin B6 (mg/d)": 1.0, "Folate (µg/d)": 300, "Vitamin B12 (µg/d)": 1.8,
            "Pantothenic Acid (mg/d)": 4, "Biotin (µg/d)": 20, "Choline (mg/d)": 375
        },
        "14-18 y": {
            "Vitamin A (µg/d)": 900, "Vitamin C (mg/d)": 75, "Vitamin D (µg/d)": 15, "Vitamin E (mg/d)": 15,
            "Vitamin K (µg/d)": 75, "Thiamin (mg/d)": 1.2, "Riboflavin (mg/d)": 1.3, "Niacin (mg/d)": 16,
            "Vitamin B6 (mg/d)": 1.3, "Folate (µg/d)": 400, "Vitamin B12 (µg/d)": 2.4,
            "Pantothenic Acid (mg/d)": 5, "Biotin (µg/d)": 25, "Choline (mg/d)": 550
        },
        "19-30 y": {
            "Vitamin A (µg/d)": 900, "Vitamin C (mg/d)": 90, "Vitamin D (µg/d)": 15, "Vitamin E (mg/d)": 15,
            "Vitamin K (µg/d)": 120, "Thiamin (mg/d)": 1.2, "Riboflavin (mg/d)": 1.3, "Niacin (mg/d)": 16,
            "Vitamin B6 (mg/d)": 1.3, "Folate (µg/d)": 400, "Vitamin B12 (µg/d)": 2.4,
            "Pantothenic Acid (mg/d)": 5, "Biotin (µg/d)": 30, "Choline (mg/d)": 550
        },
        "31-50 y": {
            "Vitamin A (µg/d)": 900, "Vitamin C (mg/d)": 90, "Vitamin D (µg/d)": 15, "Vitamin E (mg/d)": 15,
            "Vitamin K (µg/d)": 120, "Thiamin (mg/d)": 1.2, "Riboflavin (mg/d)": 1.3, "Niacin (mg/d)": 16,
            "Vitamin B6 (mg/d)": 1.3, "Folate (µg/d)": 400, "Vitamin B12 (µg/d)": 2.4,
            "Pantothenic Acid (mg/d)": 5, "Biotin (µg/d)": 30, "Choline (mg/d)": 550
        },
        "51-70 y": {
            "Vitamin A (µg/d)": 900, "Vitamin C (mg/d)": 90, "Vitamin D (µg/d)": 15, "Vitamin E (mg/d)": 15,
            "Vitamin K (µg/d)": 120, "Thiamin (mg/d)": 1.2, "Riboflavin (mg/d)": 1.3, "Niacin (mg/d)": 16,
            "Vitamin B6 (mg/d)": 1.7, "Folate (µg/d)": 400, "Vitamin B12 (µg/d)": 2.4,
            "Pantothenic Acid (mg/d)": 5, "Biotin (µg/d)": 30, "Choline (mg/d)": 550
        },
        "> 70 y": {
            "Vitamin A (µg/d)": 900, "Vitamin C (mg/d)": 90, "Vitamin D (µg/d)": 20, "Vitamin E (mg/d)": 15,
            "Vitamin K (µg/d)": 120, "Thiamin (mg/d)": 1.2, "Riboflavin (mg/d)": 1.3, "Niacin (mg/d)": 16,
            "Vitamin B6 (mg/d)": 1.7, "Folate (µg/d)": 400, "Vitamin B12 (µg/d)": 2.4,
            "Pantothenic Acid (mg/d)": 5, "Biotin (µg/d)": 30, "Choline (mg/d)": 550
        }
    },
    "Females": {
        "9-13 y": {
            "Vitamin A (µg/d)": 600, "Vitamin C (mg/d)": 45, "Vitamin D (µg/d)": 15, "Vitamin E (mg/d)": 11,
            "Vitamin K (µg/d)": 60, "Thiamin (mg/d)": 0.9, "Riboflavin (mg/d)": 0.9, "Niacin (mg/d)": 12,
            "Vitamin B6 (mg/d)": 1.0, "Folate (µg/d)": 300, "Vitamin B12 (µg/d)": 1.8,
            "Pantothenic Acid (mg/d)": 4, "Biotin (µg/d)": 20, "Choline (mg/d)": 375
        },
        "14-18 y": {
            "Vitamin A (µg/d)": 700, "Vitamin C (mg/d)": 65, "Vitamin D (µg/d)": 15, "Vitamin E (mg/d)": 15,
            "Vitamin K (µg/d)": 75, "Thiamin (mg/d)": 1.0, "Riboflavin (mg/d)": 1.0, "Niacin (mg/d)": 14,
            "Vitamin B6 (mg/d)": 1.2, "Folate (µg/d)": 400, "Vitamin B12 (µg/d)": 2.4,
            "Pantothenic Acid (mg/d)": 5, "Biotin (µg/d)": 25, "Choline (mg/d)": 400
        },
        "19-30 y": {
            "Vitamin A (µg/d)": 700, "Vitamin C (mg/d)": 75, "Vitamin D (µg/d)": 15, "Vitamin E (mg/d)": 15,
            "Vitamin K (µg/d)": 90, "Thiamin (mg/d)": 1.1, "Riboflavin (mg/d)": 1.1, "Niacin (mg/d)": 14,
            "Vitamin B6 (mg/d)": 1.3, "Folate (µg/d)": 400, "Vitamin B12 (µg/d)": 2.4,
            "Pantothenic Acid (mg/d)": 5, "Biotin (µg/d)": 30, "Choline (mg/d)": 425
        },
        "31-50 y": {
            "Vitamin A (µg/d)": 700, "Vitamin C (mg/d)": 75, "Vitamin D (µg/d)": 15, "Vitamin E (mg/d)": 15,
            "Vitamin K (µg/d)": 90, "Thiamin (mg/d)": 1.1, "Riboflavin (mg/d)": 1.1, "Niacin (mg/d)": 14,
            "Vitamin B6 (mg/d)": 1.3, "Folate (µg/d)": 400, "Vitamin B12 (µg/d)": 2.4,
            "Pantothenic Acid (mg/d)": 5, "Biotin (µg/d)": 30, "Choline (mg/d)": 425
        },
        "51-70 y": {
            "Vitamin A (µg/d)": 700, "Vitamin C (mg/d)": 75, "Vitamin D (µg/d)": 15, "Vitamin E (mg/d)": 15,
            "Vitamin K (µg/d)": 90, "Thiamin (mg/d)": 1.1, "Riboflavin (mg/d)": 1.1, "Niacin (mg/d)": 14,
            "Vitamin B6 (mg/d)": 1.5, "Folate (µg/d)": 400, "Vitamin B12 (µg/d)": 2.4,
            "Pantothenic Acid (mg/d)": 5, "Biotin (µg/d)": 30, "Choline (mg/d)": 425
        },
        "> 70 y": {
            "Vitamin A (µg/d)": 700, "Vitamin C (mg/d)": 75, "Vitamin D (µg/d)": 20, "Vitamin E (mg/d)": 15,
            "Vitamin K (µg/d)": 90, "Thiamin (mg/d)": 1.1, "Riboflavin (mg/d)": 1.1, "Niacin (mg/d)": 14,
            "Vitamin B6 (mg/d)": 1.5, "Folate (µg/d)": 400, "Vitamin B12 (µg/d)": 2.4,
            "Pantothenic Acid (mg/d)": 5, "Biotin (µg/d)": 30, "Choline (mg/d)": 425
        }
    }
}


MINERALS =  {
    "Infants": {
        "0-6 mo": {
            "Calcium (mg/d)": 200, "Chromium (µg/d)": 0.2, "Copper (µg/d)": 200, "Fluoride (mg/d)": 0.01,
            "Iodine (µg/d)": 110, "Iron (mg/d)": 0.27, "Magnesium (mg/d)": 30, "Manganese (mg/d)": 0.003,
            "Molybdenum (µg/d)": 2, "Phosphorus (mg/d)": 100, "Selenium (µg/d)": 15, "Zinc (mg/d)": 2,
            "Potassium (mg/d)": 400, "Sodium (mg/d)": 110, "Chloride (g/d)": 0.18
        },
        "7-12 mo": {
            "Calcium (mg/d)": 260, "Chromium (µg/d)": 5.5, "Copper (µg/d)": 220, "Fluoride (mg/d)": 0.5,
            "Iodine (µg/d)": 130, "Iron (mg/d)": 11, "Magnesium (mg/d)": 75, "Manganese (mg/d)": 0.6,
            "Molybdenum (µg/d)": 3, "Phosphorus (mg/d)": 275, "Selenium (µg/d)": 20, "Zinc (mg/d)": 3,
            "Potassium (mg/d)": 860, "Sodium (mg/d)": 370, "Chloride (g/d)": 0.57
        }
    },
    "Children": {
        "1-3 y": {
            "Calcium (mg/d)": 700, "Chromium (µg/d)": 11, "Copper (µg/d)": 340, "Fluoride (mg/d)": 0.7,
            "Iodine (µg/d)": 90, "Iron (mg/d)": 7, "Magnesium (mg/d)": 80, "Manganese (mg/d)": 1.2,
            "Molybdenum (µg/d)": 17, "Phosphorus (mg/d)": 460, "Selenium (µg/d)": 20, "Zinc (mg/d)": 3,
            "Potassium (mg/d)": 2000, "Sodium (mg/d)": 800, "Chloride (g/d)": 1.5
        },
        "4-8 y": {
            "Calcium (mg/d)": 1000, "Chromium (µg/d)": 15, "Copper (µg/d)": 440, "Fluoride (mg/d)": 1,
            "Iodine (µg/d)": 90, "Iron (mg/d)": 10, "Magnesium (mg/d)": 130, "Manganese (mg/d)": 1.5,
            "Molybdenum (µg/d)": 22, "Phosphorus (mg/d)": 500, "Selenium (µg/d)": 30, "Zinc (mg/d)": 5,
            "Potassium (mg/d)": 2300, "Sodium (mg/d)": 1000, "Chloride (g/d)": 1.9
        }
    },
    "Males": {
        "9-13 y": {
            "Calcium (mg/d)": 1300, "Chromium (µg/d)": 25, "Copper (µg/d)": 700, "Fluoride (mg/d)": 2,
            "Iodine (µg/d)": 120, "Iron (mg/d)": 8, "Magnesium (mg/d)": 240, "Manganese (mg/d)": 1.9,
            "Molybdenum (µg/d)": 34, "Phosphorus (mg/d)": 1250, "Selenium (µg/d)": 40, "Zinc (mg/d)": 8,
            "Potassium (mg/d)": 2500, "Sodium (mg/d)": 1200, "Chloride (g/d)": 2.3
        },
        "14-18 y": {
            "Calcium (mg/d)": 1300, "Chromium (µg/d)": 35, "Copper (µg/d)": 890, "Fluoride (mg/d)": 3,
            "Iodine (µg/d)": 150, "Iron (mg/d)": 11, "Magnesium (mg/d)": 410, "Manganese (mg/d)": 2.2,
            "Molybdenum (µg/d)": 43, "Phosphorus (mg/d)": 1250, "Selenium (µg/d)": 55, "Zinc (mg/d)": 11,
            "Potassium (mg/d)": 3000, "Sodium (mg/d)": 1500, "Chloride (g/d)": 2.3
        },
        "19-30 y": {
            "Calcium (mg/d)": 1000, "Chromium (µg/d)": 35, "Copper (µg/d)": 900, "Fluoride (mg/d)": 4,
            "Iodine (µg/d)": 150, "Iron (mg/d)": 8, "Magnesium (mg/d)": 400, "Manganese (mg/d)": 2.3,
            "Molybdenum (µg/d)": 45, "Phosphorus (mg/d)": 700, "Selenium (µg/d)": 55, "Zinc (mg/d)": 11,
            "Potassium (mg/d)": 3400, "Sodium (mg/d)": 1500, "Chloride (g/d)": 2.3
        },
        "31-50 y": {
            "Calcium (mg/d)": 1000, "Chromium (µg/d)": 35, "Copper (µg/d)": 900, "Fluoride (mg/d)": 4,
            "Iodine (µg/d)": 150, "Iron (mg/d)": 8, "Magnesium (mg/d)": 420, "Manganese (mg/d)": 2.3,
            "Molybdenum (µg/d)": 45, "Phosphorus (mg/d)": 700, "Selenium (µg/d)": 55, "Zinc (mg/d)": 11,
            "Potassium (mg/d)": 3400, "Sodium (mg/d)": 1500, "Chloride (g/d)": 2.3
        },
        "51-70 y": {
            "Calcium (mg/d)": 1000, "Chromium (µg/d)": 30, "Copper (µg/d)": 900, "Fluoride (mg/d)": 4,
            "Iodine (µg/d)": 150, "Iron (mg/d)": 8, "Magnesium (mg/d)": 420, "Manganese (mg/d)": 2.3,
            "Molybdenum (µg/d)": 45, "Phosphorus (mg/d)": 700, "Selenium (µg/d)": 55, "Zinc (mg/d)": 11,
            "Potassium (mg/d)": 3400, "Sodium (mg/d)": 1500, "Chloride (g/d)": 2.0
        },
        "> 70 y": {
            "Calcium (mg/d)": 1200, "Chromium (µg/d)": 30, "Copper (µg/d)": 900, "Fluoride (mg/d)": 4,
            "Iodine (µg/d)": 150, "Iron (mg/d)": 8, "Magnesium (mg/d)": 420, "Manganese (mg/d)": 2.3,
            "Molybdenum (µg/d)": 45, "Phosphorus (mg/d)": 700, "Selenium (µg/d)": 55, "Zinc (mg/d)": 11,
            "Potassium (mg/d)": 3400, "Sodium (mg/d)": 1500, "Chloride (g/d)": 1.8
        }
    },
    "Females": {
        "9-13 y": {
            "Calcium (mg/d)": 1300, "Chromium (µg/d)": 21, "Copper (µg/d)": 700, "Fluoride (mg/d)": 2,
            "Iodine (µg/d)": 120, "Iron (mg/d)": 8, "Magnesium (mg/d)": 240, "Manganese (mg/d)": 1.6,
            "Molybdenum (µg/d)": 34, "Phosphorus (mg/d)": 1250, "Selenium (µg/d)": 40, "Zinc (mg/d)": 8,
            "Potassium (mg/d)": 2300, "Sodium (mg/d)": 1200, "Chloride (g/d)": 2.3
        },
        "14-18 y": {
            "Calcium (mg/d)": 1300, "Chromium (µg/d)": 24, "Copper (µg/d)": 890, "Fluoride (mg/d)": 3,
            "Iodine (µg/d)": 150, "Iron (mg/d)": 15, "Magnesium (mg/d)": 360, "Manganese (mg/d)": 1.6,
            "Molybdenum (µg/d)": 43, "Phosphorus (mg/d)": 1250, "Selenium (µg/d)": 55, "Zinc (mg/d)": 9,
            "Potassium (mg/d)": 2300, "Sodium (mg/d)": 1500, "Chloride (g/d)": 2.3
        },
        "19-30 y": {
            "Calcium (mg/d)": 1000, "Chromium (µg/d)": 25, "Copper (µg/d)": 900, "Fluoride (mg/d)": 3,
            "Iodine (µg/d)": 150, "Iron (mg/d)": 18, "Magnesium (mg/d)": 310, "Manganese (mg/d)": 1.8,
            "Molybdenum (µg/d)": 45, "Phosphorus (mg/d)": 700, "Selenium (µg/d)": 55, "Zinc (mg/d)": 8,
            "Potassium (mg/d)": 2600, "Sodium (mg/d)": 1500, "Chloride (g/d)": 2.3
        },
        "31-50 y": {
            "Calcium (mg/d)": 1000, "Chromium (µg/d)": 25, "Copper (µg/d)": 900, "Fluoride (mg/d)": 3,
            "Iodine (µg/d)": 150, "Iron (mg/d)": 18, "Magnesium (mg/d)": 320, "Manganese (mg/d)": 1.8,
            "Molybdenum (µg/d)": 45, "Phosphorus (mg/d)": 700, "Selenium (µg/d)": 55, "Zinc (mg/d)": 8,
            "Potassium (mg/d)": 2600, "Sodium (mg/d)": 1500, "Chloride (g/d)": 2.3
        },
        "51-70 y": {
            "Calcium (mg/d)": 1200, "Chromium (µg/d)": 20, "Copper (µg/d)": 900, "Fluoride (mg/d)": 3,
            "Iodine (µg/d)": 150, "Iron (mg/d)": 8, "Magnesium (mg/d)": 320, "Manganese (mg/d)": 1.8,
            "Molybdenum (µg/d)": 45, "Phosphorus (mg/d)": 700, "Selenium (µg/d)": 55, "Zinc (mg/d)": 8,
            "Potassium (mg/d)": 2600, "Sodium (mg/d)": 1500, "Chloride (g/d)": 2.0
        },
        "> 70 y": {
            "Calcium (mg/d)": 1200, "Chromium (µg/d)": 20, "Copper (µg/d)": 900, "Fluoride (mg/d)": 3,
            "Iodine (µg/d)": 150, "Iron (mg/d)": 8, "Magnesium (mg/d)": 320, "Manganese (mg/d)": 1.8,
            "Molybdenum (µg/d)": 45, "Phosphorus (mg/d)": 700, "Selenium (µg/d)": 55, "Zinc (mg/d)": 8,
            "Potassium (mg/d)": 2600, "Sodium (mg/d)": 1500, "Chloride (g/d)": 1.8
        }
    }
}
