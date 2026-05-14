from langchain_core.tools import tool


@tool
def policy_lookup_tool(
    category: str
) -> str:
    """
    Get expense policy.
    """

    policies = {
        "Travel":
            "Travel under $3000 allowed.",
        "Food":
            "Meals over $200 require approval."
    }

    return policies.get(
        category,
        "No policy found."
    )
