from langchain_agent.agent import (
    agent
)

expense = """
Employee: Yuan Li
Amount: 8000
Category: Travel

Analyze this expense.
"""

result = agent.invoke({
    "input": expense
})

print("\nFINAL RESULT:\n")

print(
    result["output"]
)