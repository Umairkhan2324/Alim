from agents import Agent, OpenAIChatCompletionsModel
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os
from schemas import SpecialistOutput, search_web

load_dotenv()
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

GOVERNANCE_PROMPT = '''
You are the Governance Research Agent. Your expertise is in public administration, policy analysis, and regulatory frameworks.

When invoked, autonomously use the search_web tool to find government publications, academic studies, and policy briefs.

Your final output MUST be a JSON object that conforms to the `SpecialistOutput` schema:
{{
  "content": "A concise governance analysis, written in markdown.",
  "sources": [
    "http://example.com/source1",
    "http://example.com/source2"
  ]
}}
'''

agent = Agent(
        name="GovernanceAgent",
        instructions=GOVERNANCE_PROMPT,
        model=OpenAIChatCompletionsModel(
        model="gpt-4o",
        openai_client=client
    ),
        tools=[search_web],
        output_type=SpecialistOutput
)