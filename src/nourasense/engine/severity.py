from enum import Enum

class BurdenClass(Enum):
    EXTREME_BURDEN = "EXTREME BURDEN"
    TRIPLE_BURDEN = "TRIPLE BURDEN"
    DOUBLE_BURDEN = "DOUBLE BURDEN"
    SINGLE_BURDEN = "SINGLE BURDEN"
    NO_BURDEN = "NO BURDEN"

class SeverityClass(Enum):
    NORMAL = 'NORMAL' # z-score is within ±2
    CONCERNING = 'CONCERNING' # z-score is between ±2 and ±3
    CRITICAL = 'CRITICAL' # z-score is beyond ±3

class SeverityClassifier:
    def __init__(self, z_scores: dict, threshold: int = 2):
        self.z_scores = z_scores
        self.threshold = threshold
        
    def classify_burden(self) -> str:
        
        critical_count = sum(1 for z in self.z_scores.values() if abs(z) > self.threshold)

        if critical_count >= 4:
            return BurdenClass.EXTREME_BURDEN.value
        elif critical_count == 3:
            return BurdenClass.TRIPLE_BURDEN.value
        elif critical_count == 2:
            return BurdenClass.DOUBLE_BURDEN.value
        elif critical_count == 1:
            return BurdenClass.SINGLE_BURDEN.value
        else:
            return BurdenClass.NO_BURDEN.value

    def classify_severity(self) -> dict:

        severity = {}

        for indicator, z_score in self.z_scores.items():
            if abs(z_score) < 2:
                severity[indicator] = SeverityClass.NORMAL.value
            elif 2 <= abs(z_score) < 3:
                severity[indicator] = SeverityClass.CONCERNING.value
            else:
                severity[indicator] = SeverityClass.CRITICAL.value

        return severity