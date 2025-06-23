from agents import Agent, OpenAIChatCompletionsModel, WebSearchTool
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os
from schemas import SpecialistOutput
load_dotenv()
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

ECONOMICS_PROMPT = '''
You are the Economics Research Agent. Your expertise is in macroeconomic indicators, financial markets, and economic policy.

When invoked, autonomously plan a multi-step research approach using the WebSearch tool to find relevant information.

Your final output MUST be a JSON object that conforms to the `SpecialistOutput` schema:
{{
  "content": "A concise economic analysis, written in markdown.",
  "sources": [
    "http://example.com/source1",
    "http://example.com/source2"
  ]
}}
'''

tools = [WebSearchTool()]
agent = Agent(
    name="EconomicsAgent",
    instructions=ECONOMICS_PROMPT,
    model=OpenAIChatCompletionsModel(
        model="gpt-4o",
        openai_client=client
    ),
    tools=tools,
    output_type=SpecialistOutput
)