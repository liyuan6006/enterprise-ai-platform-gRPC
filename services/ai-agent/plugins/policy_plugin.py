from semantic_kernel.functions import (
    kernel_function
)


class PolicyPlugin:

    @kernel_function(
        description="Get company expense policy"
    )
    def get_policy(
        self,
        category: str
    ) -> str:

        policies = {
            "Travel":
                "Travel under $3000 is allowed.",
            "Food":
                "Meals over $200 require approval."
        }

        return policies.get(
            category,
            "No policy found."
        )