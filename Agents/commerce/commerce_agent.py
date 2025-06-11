# agents/commerce/commerce_agent.py
from agents import Agent, ModelSettings
from agents.models import OpenAIChatCompletionsModel
from agents.tools import WebSearchTool

# System prompt for the Commerce agent
SYSTEM_PROMPT = '''
You are the Commerce Research Agent. Your expertise is in trade, retail, e-commerce, and market dynamics.

When invoked, autonomously plan a multi-step research approach using the WebSearch tool:
1. Identify key terms and recent trends relevant to the user's commerce query.
2. Use WebSearch to retrieve up-to-date market reports, trade data, news articles, or analyses.
3. Summarize the most relevant findings, ensuring each fact is backed by a citation (URL or source name).
4. Provide a concise, well-structured summary of the current state of commerce for the specified topic.
'''


def create_commerce_agent():
    # Initialize the underlying LLM
    llm = OpenAIChatCompletionsModel(
        model="gpt-4o"
    )

    # Register the WebSearch tool
    tools = [WebSearchTool()]

    # Create the Agent
    agent = Agent(
        name="CommerceAgent",
        system_prompt=SYSTEM_PROMPT,
        model=llm,
        tools=tools,
        settings=ModelSettings(
            temperature=0.0,
            parallel_tool_calls=False  # single-agent internal flow
        )
    )
    return agent