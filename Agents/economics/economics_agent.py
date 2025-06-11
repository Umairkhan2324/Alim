from agents import Agent, ModelSettings, OpenAIChatCompletionsModel, WebSearchTool
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os
load_dotenv()
OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

ECONOMICS_PROMPT = '''
You are the Economics Research Agent. Your expertise is in macroeconomic indicators, financial markets, and economic policy.

When invoked, autonomously plan a multi-step research approach using tools:
1. Identify key economic terms and indicators.
2. Use WebSearch to retrieve economic reports, academic papers, and data.
3. Summarize major economic theories and findings with citations.
4. Provide a concise economic analysis for the query.
'''

tools = [WebSearchTool()]
agent = Agent(
    name="EconomicsAgent",
    instructions=ECONOMICS_PROMPT,
    model=OpenAIChatCompletionsModel(
        model="gpt-4o",
        openai_client=client
    ),
    tools=tools
)