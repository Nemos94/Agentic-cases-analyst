from enum import Enum
from typing import Dict, List

class CaseStatus(Enum):
    IN_PROGRESS = "in_progress"
    CONCLUDED = "concluded"
    ESCALATED = "ESCALATED"

class CaseState:
    def __init__(self, email_text : str):
        #core input
        self.email_text: str = email_text

        #extracted / derived information
        self.extracted_data: Dict[str, str] = {}
        self.missing_info_flags: List[str] = []

        #confidence level
        self.confidence: str = "low"

        #Reasoning transparency
        self.reasoning_trace: List[str] = []
        self.current_action: str | None = None

        #Loop control
        self.iteration: int = 0
        self.status: CaseStatus = CaseStatus.IN_PROGRESS

    # ---------- State update helpers ----------

    def add_extracted_date(self, key:str, value: str):
        self.extracted_data[key] = value

    def add_missing_info(self, info:str):
        if info not in self.missing_info_flags:
            self.missing_info_flags.append(info)

    def clear_missing_info(self, info: str):
        if info in self.missing_info_flags:
            self.missing_info_flags.remove(info)

    def update_confidence(self, level:str):
        if level not in ["low", "medium", "high"]:
                raise ValueError("Confidence must be: low, medium, or high")
        self.confidence = level

    def log_reasoning(self, message: str):
        self.reasoning_trace.append(
            f"Iteration {self.iteration}: {message}"
        )

    # ---------- Loop control ----------

    def next_iteration(self):
        self.iteration += 1

    def conclude(self):
        self.status = CaseStatus.CONCLUDED
        self.current_action = "CONCLUDE"

    def escalate(self, reason: str):
        self.status = CaseStatus.ESCALATED
        self.current_action = "ESCALATE"
        self.log_reasoning(f"Escalated: {reason}")

    # ---------- Output ----------

    def summary(self) -> Dict:
        return {
            "status": self.status.value,
            "confidence": self.confidence,
            "extracted_data": self.extracted_data,
            "missing_info": self.missing_info_flags,
            "reasoning_trace": self.reasoning_trace,

        }

#{
#  "status": "concluded",
#  "confidence": "high",
#  "extracted_data": {...},
#  "missing_info": [...],
#  "reasoning_trace": [...]
#}

#if __name__ == "__main__":
#    state = CaseState("Test email)
#    print(state.summary())