from agents import Agent, OpenAIChatCompletionsModel, WebSearchTool
from dotenv import load_dotenv
from openai import AsyncOpenAI  
import os
from schemas import SpecialistOutput
load_dotenv()
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))


FA_PROMPT = '''
You are the Foreign Affairs Research Agent. Your expertise is in international diplomacy, geopolitical analysis, and foreign policy.

When invoked, autonomously use the WebSearch tool to find government reports, think tank analyses, and news.

Your final output MUST be a JSON object that conforms to the `SpecialistOutput` schema:
{{
  "content": "A concise geopolitical overview, written in markdown.",
  "sources": [
    "http://example.com/source1",
    "http://example.com/source2"
  ]
}}
'''


tools = [WebSearchTool()]
agent = Agent(  
    name="ForeignAffairsAgent",
    instructions=FA_PROMPT,
    model=OpenAIChatCompletionsModel(
        model="gpt-4o",
        openai_client=client
    ),
    tools=tools,
    output_type=SpecialistOutput
)