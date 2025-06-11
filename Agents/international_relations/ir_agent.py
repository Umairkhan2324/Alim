from agents import Agent, ModelSettings, OpenAIChatCompletionsModel, WebSearchTool
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os
load_dotenv()
OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

IR_PROMPT = '''
You are the International Relations Research Agent. Your expertise is in global affairs, political science, and international security.

When invoked, autonomously plan a multi-step research approach using tools:
1. Identify key geopolitical actors, treaties, and conflicts.
2. Use WebSearch to retrieve scholarly articles, policy journals, and news analysis.
3. Summarize major international events and their implications with citations.
4. Provide a concise analysis of international relations for the query.
'''


tools = [WebSearchTool()]
agent = Agent(
    name="InternationalRelationsAgent",
    instructions=IR_PROMPT,
    model=OpenAIChatCompletionsModel(
        model="gpt-4o",
        openai_client=client
    ),
    tools=tools
)