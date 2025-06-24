from agents import Agent, OpenAIChatCompletionsModel
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os
from schemas import SpecialistOutput, search_web

load_dotenv()
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

ENTREPRENEURSHIP_PROMPT = '''
You are the Entrepreneurship Research Agent. Your expertise is in startups, venture capital, and innovation ecosystems.

When invoked, autonomously use the search_web tool to find case studies, funding data, and market analysis.

Your final output MUST be a JSON object that conforms to the `SpecialistOutput` schema:
{{
  "content": "A concise and informative summary of entrepreneurial insights, written in markdown.",
  "sources": [
    "http://example.com/source1",
    "http://example.com/source2"
  ]
}}
'''

agent = Agent(
    name="EntrepreneurshipAgent",
    instructions=ENTREPRENEURSHIP_PROMPT,
    model=OpenAIChatCompletionsModel(
        model="gpt-4o",
        openai_client=client
    ),
    tools=[search_web],
    output_type=SpecialistOutput
)