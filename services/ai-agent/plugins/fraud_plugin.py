from semantic_kernel.functions import (
    kernel_function
)

from fraud_client import (
    check_fraud
)


class FraudPlugin:

    @kernel_function(
        description="Analyze fraud risk"
    )
    def analyze_fraud(
        self,
        employee_name: str,
        amount: float,
        category: str
    ) -> str:

        expense = {
            "employee_name": employee_name,
            "amount": amount,
            "category": category
        }

        result = check_fraud(
            expense
        )

        return str(result)