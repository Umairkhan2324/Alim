# agents/current_affairs/current_affairs_agent.py
from agents import Agent, OpenAIChatCompletionsModel
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os
from schemas import SpecialistOutput, search_web

load_dotenv()
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# System prompt for the Current Affairs agent
ca_prompt = '''
You are the Current Affairs Research Agent. Your expertise is in gathering the most recent and relevant news, events, and developments on a given topic.

When invoked, autonomously plan a multi-step research approach using the search_web tool to find up-to-date information.

Your final output MUST be a JSON object that conforms to the `SpecialistOutput` schema:
{{
  "content": "A concise summary of the latest developments, written in markdown.",
  "sources": [
    "http://example.com/source1",
    "http://example.com/source2"
  ]
}}
'''

# Create the Agent
agent = Agent(
        name="CurrentAffairsAgent",
        instructions=ca_prompt,
        model=OpenAIChatCompletionsModel(
        model="gpt-4o",
        openai_client=client
    ),
    tools=[search_web],
    output_type=SpecialistOutput
)

# return agent