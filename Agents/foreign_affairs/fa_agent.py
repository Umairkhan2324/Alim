from agents import Agent, ModelSettings, OpenAIChatCompletionsModel, WebSearchTool
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os
load_dotenv()
OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))


FA_PROMPT = '''
You are the Foreign Affairs Research Agent. Your expertise is in international diplomacy, geopolitical analysis, and foreign policy.

When invoked, autonomously plan a multi-step research approach using tools:
1. Identify key countries, regions, and geopolitical issues.
2. Use WebSearch to retrieve government reports, think tank analyses, and news.
3. Summarize major foreign policy developments and events with citations.
4. Provide a concise geopolitical overview for the query.
'''


tools = [WebSearchTool()]
agent = Agent(
    name="ForeignAffairsAgent",
    instructions=FA_PROMPT,
    model=OpenAIChatCompletionsModel(
        model="gpt-4o",
        openai_client=client
    ),
    tools=tools
)