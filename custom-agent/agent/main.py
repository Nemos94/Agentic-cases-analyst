from state import CaseState
from agent import CaseAnalystAgent
from openai import OpenAI

state = CaseState(
    "I am very dissatisfied. I have complained several times and no one responds."
)
state.add_missing_info("product")

agent = CaseAnalystAgent()
final_state = agent.run(state)

print(final_state.summary())


email = "The system isn't working and no one is responding."

state = CaseState(email)
state.add_missing_info("product")

agent = CaseAnalystAgent()
final_state = agent.run(state)

print(final_state.summary())