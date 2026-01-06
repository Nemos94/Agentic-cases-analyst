from openai import OpenAI
from state import CaseState, CaseStatus
import json

MAX_ITERATIONS = 3

client = OpenAI()

class CaseAnalystAgent:
    def _init_(self):
        pass

    def run(self, state: CaseState) -> CaseState:
        while state.iteration < MAX_ITERATIONS and state.status == CaseStatus.IN_PROGRESS:
            state.next_iteration()
            state.log_reasoning("Start analysis step")

            action = self.decide_next_action(state)

            if action == "ESCALATE":
                state.escalate("Risk or ambiguity too high")
                break

            if action == "CONCLUDE":
                state.conclude()
                state.log_reasoning("Sufficient information for human action")
                break

            if action == "REQUEST_CONTEXT":
                self.request_context(state)

            if action == "CONSULT_HISTORY":
                self.consult_history(state)
        
        # Safety net: max iterations reached
        if state.status == CaseStatus.IN_PROGRESS:
            state.escalate("Max iterations reached without resolution")

            return state
        
    # ---------- Decision Logic (Rule-based for now) ----------

    # def decide_next_action(self, state: CaseState) -> str:
        # Escalate if legal/financial risk detected
        # if "legal" in state.email_text.lower() or "invoice" in state.email_text.lower():
        #     return "ESCALATE"

        # Missing critical info
        # if state.missing_info_flags:
           #  return "REQUEST_CONTEXT"
        
        # Low confidence after first iteration → consult history
        # if state.confidence == "low" and state.iteration < 2:
            # return "CONSULT_HISTORY"
        
        #Default: conclude
        # return "CONCLUDE"

        #new decide next action with GPT
    def decide_next_action(self, state:CaseState) -> str:
        prompt = self.build_decision_prompt(state)

        response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0

        )

        content = response.choices[0].message.content

        try:
            decision = json.loads(content)
            action = decision.get("action")
            reason = decision.get("reason", "")

            state.log_reasoning(f"LLM decision: {action} – {reason}")
        
            if action not in ["CONCLUDE", "REQUEST_CONTEXT", "CONSULT_HISTORY", "ESCALATE"]:
                raise ValueError("Invalid aCtion returned by LLM")

            return action
        
        except Exception as e:
            state.log_reasoning(f"LLM error or invalid output: {str(e)}")
            return "ESCALATE"

    # ---------- Actions ----------
    def request_context(self, state: CaseState):
        state.log_reasoning(f"Requesting more context. Missing info: {state.missing_info_flags}")
    
    def consult_history(self, state: CaseState):
        state.log_reasoning("Consulting historical context (mocked)")
        # Mocked improvement after consulting history
        state.update_confidence("medium")


    def build_decision_prompt(self, state: CaseState) -> str:
        return f"""
        You are a Case Analyst AI.

        Your task is to decide the NEXT ACTION to take.
        You must choose ONE of the following actions:
        - CONCLUDE
        - REQUEST_CONTEXT
        - CONSULT_HISTORY
        - ESCALATE

        Rules:
        - Escalate if legal or financial risk is present
        - Escalate if ambiguity is high
        - Request context if critical information is missing
        - Conclude only if a human can act without rework
        - Do NOT invent information

        Case email:
        {state.email_text}

        Extracted data:
        {state.extracted_data}

        Missing information:
        {state.missing_info_flags}

        Confidence level:
        {state.confidence}

        Respond ONLY in valid JSON:
        {{
        "action": "<ONE_ACTION>",
        "reason": "<short explanation>"
        }}
        """
