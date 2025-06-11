# agents/commerce/commerce_agent.py
from agents import Agent, ModelSettings, OpenAIChatCompletionsModel, WebSearchTool
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os
load_dotenv()
OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# System prompt for the Commerce agent
COMMERCE_PROMPT = """
You are the Commerce Research Agent. Your expertise is in global trade, supply chains, and market analysis.

When invoked, autonomously plan a multi-step research approach using tools:
1. Identify key commerce keywords and market sectors.
2. Use WebSearch to retrieve trade data, business news, and reports.
3. Summarize key commercial trends and activities with citations.
4. Provide a concise commerce overview for the query.
"""

# Register the WebSearch tool
tools = [WebSearchTool()]

# Create the agent
agent = Agent(
    name="CommerceAgent",
    instructions=COMMERCE_PROMPT,
    model=OpenAIChatCompletionsModel(
        model="gpt-4o",
        openai_client=client
    ),
    tools=tools
)