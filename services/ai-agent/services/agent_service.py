import os

from semantic_kernel import Kernel

from semantic_kernel.connectors.ai.open_ai import (
    OpenAIChatCompletion
)

from semantic_kernel.connectors.ai.function_choice_behavior import (
    FunctionChoiceBehavior
)

from semantic_kernel.contents.chat_history import (
    ChatHistory
)

from plugins.fraud_plugin import (
    FraudPlugin
)

from plugins.policy_plugin import (
    PolicyPlugin
)


class AgentService:

    def __init__(self):

        self.kernel = Kernel()

        self.kernel.add_service(
            OpenAIChatCompletion(
                service_id="chat",
                api_key=os.getenv(
                    "OPENAI_API_KEY"
                ),
                ai_model_id="gpt-4.1-mini"
            )
        )

        self.kernel.add_plugin(
            FraudPlugin(),
            plugin_name="Fraud"
        )

        self.kernel.add_plugin(
            PolicyPlugin(),
            plugin_name="Policy"
        )

    async def analyze_expense(
        self,
        expense
    ):

        chat_history = ChatHistory()

        chat_history.add_user_message(
            f"""
Analyze this expense.

Expense:
{expense}

Determine:
- fraud risk
- compliance risk
- business risk

Use available plugins if needed.
"""
        )

        settings = self.kernel.get_prompt_execution_settings_from_service_id(
            "chat"
        )

        settings.function_choice_behavior = (
            FunctionChoiceBehavior.Auto()
        )

        response = await self.kernel.invoke_prompt(
            chat_history.messages[-1].content,
            settings=settings
        )

        return str(response)