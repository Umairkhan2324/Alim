from agents import Agent, OpenAIChatCompletionsModel
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os
from schemas import SpecialistOutput, search_web
load_dotenv()
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))


FINANCE_PROMPT = '''
You are the Finance Research Agent. You will provide statistical analysis of the data provided to you, and will alays give numbers to prove your report and analysis. Your expertise is in financial markets, investment analysis, and corporate finance.

When invoked, autonomously use the search_web tool to find market data, financial news, and company reports.

Your final output MUST be a JSON object that conforms to the `SpecialistOutput` schema:
{{
  "content": "A concise financial analysis, written in markdown.",
  "sources": [
    "http://example.com/source1",
    "http://example.com/source2"
  ]
}}
'''


agent = Agent(
    name="FinanceAgent",
    instructions=FINANCE_PROMPT,
    model=OpenAIChatCompletionsModel(
        model="gpt-4o",
        openai_client=client
    ),
    tools=[search_web],
    output_type=SpecialistOutput
)
