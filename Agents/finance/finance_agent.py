from agents import Agent, ModelSettings, OpenAIChatCompletionsModel, WebSearchTool
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os
load_dotenv()
OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))


FINANCE_PROMPT = '''
You are the Finance Research Agent. Your expertise is in financial markets, investment analysis, and corporate finance.

When invoked, autonomously plan a multi-step research approach using tools:
1. Identify key financial terms, metrics, and assets.
2. Use WebSearch to retrieve market data, financial news, and company reports.
3. Summarize key financial insights and performance with citations.
4. Provide a concise financial analysis for the query.
'''


tools = [WebSearchTool()]
agent = Agent(
    name="FinanceAgent",
    instructions=FINANCE_PROMPT,
    model=OpenAIChatCompletionsModel(
        model="gpt-4o",
        openai_client=client
    ),
    tools=tools
)
