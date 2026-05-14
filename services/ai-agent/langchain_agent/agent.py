import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(
    Path(__file__).resolve().parents[1] / ".env"
)

from langchain_openai import (
    ChatOpenAI
)

from langchain_core.messages import (
    HumanMessage,
    ToolMessage
)

from langchain_agent.tools.fraud_tool import (
    fraud_check_tool
)

from langchain_agent.tools.policy_tool import (
    policy_lookup_tool
)


llm = ChatOpenAI(
    model="gpt-4.1-mini",
    api_key=os.getenv(
        "OPENAI_API_KEY"
    ),
    temperature=0
)

tools = [
    fraud_check_tool,
    policy_lookup_tool
]


class ToolCallingAgent:

    def __init__(
        self,
        llm,
        tools
    ):
        self.llm = llm.bind_tools(
            tools
        )
        self.tools_by_name = {
            tool.name: tool
            for tool in tools
        }
        self.messages = []

    def invoke(
        self,
        inputs
    ):
        user_input = inputs.get(
            "input",
            inputs
        )

        self.messages.append(
            HumanMessage(
                content=str(user_input)
            )
        )

        response = self.llm.invoke(
            self.messages
        )
        self.messages.append(
            response
        )

        while response.tool_calls:
            for tool_call in response.tool_calls:
                tool = self.tools_by_name[
                    tool_call["name"]
                ]
                tool_result = tool.invoke(
                    tool_call["args"]
                )
                self.messages.append(
                    ToolMessage(
                        content=str(tool_result),
                        tool_call_id=tool_call["id"]
                    )
                )

            response = self.llm.invoke(
                self.messages
            )
            self.messages.append(
                response
            )

        return {
            "output": response.content
        }


agent = ToolCallingAgent(
    llm=llm,
    tools=tools
)
