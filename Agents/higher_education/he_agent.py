from agents import Agent, OpenAIChatCompletionsModel
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os
from schemas import SpecialistOutput, search_web

load_dotenv()
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

HE_PROMPT = '''
You are the Higher Education Research Agent. Your expertise is in university systems, academic trends, and educational policy.

When invoked, autonomously use the search_web tool to find academic journals, university reports, and policy studies.

Your final output MUST be a JSON object that conforms to the `SpecialistOutput` schema:
{{
  "content": "A concise overview of the higher education landscape, written in markdown.",
  "sources": [
    "http://example.com/source1",
    "http://example.com/source2"
  ]
}}
'''

agent = Agent(
    name="HigherEducationAgent",
    instructions=HE_PROMPT,
    model=OpenAIChatCompletionsModel(
        model="gpt-4o",
        openai_client=client
    ),
    tools=[search_web],
    output_type=SpecialistOutput
)