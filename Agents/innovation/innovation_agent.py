from agents import Agent, ModelSettings, OpenAIChatCompletionsModel, WebSearchTool
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os
load_dotenv()
OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

INNOVATION_PROMPT = '''
You are the Innovation Research Agent. Your expertise is in technology adoption, disruptive trends, and R&D strategies.

When invoked, autonomously plan a multi-step research approach using tools:
1. Identify key innovation concepts and technology areas.
2. Use WebSearch to retrieve patent filings, research papers, and market analyses.
3. Summarize key innovative breakthroughs and their impact with citations.
4. Provide a concise innovation report for the query.
'''


tools = [WebSearchTool()]
agent = Agent(
    name="InnovationAgent",
    instructions=INNOVATION_PROMPT,
    model=OpenAIChatCompletionsModel(
        model="gpt-4o",
        openai_client=client
    ),
    tools=tools
)
