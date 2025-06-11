from agents import Agent, ModelSettings,OpenAIChatCompletionsModel, WebSearchTool
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os
load_dotenv()
OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

TECH_PROMPT = '''
You are the Technology Research Agent. Your expertise is in emerging technologies, industry trends, and technical analysis.

When invoked, autonomously plan a multi-step research approach using tools:
1. Identify key technology keywords and domains.
2. Use WebSearch to retrieve tech articles, whitepapers, and reports.
3. Summarize major technological developments with citations.
4. Provide a concise technology overview for the query.
'''


tools = [WebSearchTool()]
agent = Agent(
    name="TechnologyAgent",
    instructions=TECH_PROMPT,
    model=OpenAIChatCompletionsModel(
    model="gpt-4o",
    openai_client=client
    ),
    tools=tools
)

# return agent