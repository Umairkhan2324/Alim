from agents import Agent, OpenAIChatCompletionsModel, WebSearchTool
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os
from schemas import SpecialistOutput
load_dotenv()
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))


FINANCE_PROMPT = '''
You are the Finance Research Agent. Your expertise is in financial markets, investment analysis, and corporate finance.

When invoked, autonomously use the WebSearch tool to find market data, financial news, and company reports.

Your final output MUST be a JSON object that conforms to the `SpecialistOutput` schema:
{{
  "content": "A concise financial analysis, written in markdown.",
  "sources": [
    "http://example.com/source1",
    "http://example.com/source2"
  ]
}}
'''


tools = [WebSearchTool()]
agent = Agent(
    name="FinanceAgent",
    instructions=FINANCE_PROMPT,
    model=OpenAIChatCompletionsModel(
        model="gpt-4o",
        openai_client=client
    ),
    tools=tools,
    output_type=SpecialistOutput
)
