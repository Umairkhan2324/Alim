from agents import Agent, OpenAIChatCompletionsModel
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os
from schemas import SpecialistOutput, search_web

load_dotenv()
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

IR_PROMPT = '''
You are the International Relations Research Agent. Your expertise is in global affairs, political science, and international security.

When invoked, autonomously use the search_web tool to find scholarly articles, policy journals, and news analysis.

Your final output MUST be a JSON object that conforms to the `SpecialistOutput` schema:
{{
  "content": "A concise analysis of international relations, written in markdown.",
  "sources": [
    "http://example.com/source1",
    "http://example.com/source2"
  ]
}}
'''

agent = Agent(
    name="InternationalRelationsAgent",
    instructions=IR_PROMPT,
    model=OpenAIChatCompletionsModel(
        model="gpt-4o",
        openai_client=client
    ),
    tools=[search_web],
    output_type=SpecialistOutput
)