from langchain_core.tools import tool

from fraud_client import (
    check_fraud
)


@tool
def fraud_check_tool(
    employee_name: str,
    amount: float,
    category: str
) -> str:
    """
    Analyze fraud risk for an expense.
    """

    expense = {
        "employee_name": employee_name,
        "amount": amount,
        "category": category
    }

    result = check_fraud(
        expense
    )

    return str(result)
