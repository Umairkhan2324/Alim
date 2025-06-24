# agents/commerce/commerce_agent.py
from agents import Agent, OpenAIChatCompletionsModel
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os
from schemas import SpecialistOutput, search_web

load_dotenv()
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# System prompt for the Commerce agent
COMMERCE_PROMPT = """
You are the Commerce Research Agent. You will provide statistical analysis of the data provided to you, and will alays give numbers to prove your report and analysis. Your expertise is in global trade, supply chains, and market analysis.

When invoked, autonomously plan a multi-step research approach using the search_web tool to find relevant information.

Your final output MUST be a JSON object that conforms to the `SpecialistOutput` schema:
{{
  "content": "A concise overview of commercial trends and activities, written in markdown.",
  "sources": [
    "http://example.com/source1",
    "http://example.com/source2"
  ]
}}
"""

# Create the agent
agent = Agent(
    name="CommerceAgent",
    instructions=COMMERCE_PROMPT,
    model=OpenAIChatCompletionsModel(
        model="gpt-4o",
        openai_client=client
    ),
    tools=[search_web],
    output_type=SpecialistOutput
)