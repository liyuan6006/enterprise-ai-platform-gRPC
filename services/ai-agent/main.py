import asyncio

from services.agent_service import (
    AgentService
)

agent = AgentService()

expense = {
    "employee_name": "Yuan Li",
    "amount": 8000,
    "category": "Travel"
}


async def run():

    result = await agent.analyze_expense(
        expense
    )

    print("\nAI RESULT:\n")
    print(result)


asyncio.run(run())