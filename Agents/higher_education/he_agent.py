from agents import Agent, ModelSettings, OpenAIChatCompletionsModel, WebSearchTool
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os
load_dotenv()
OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))


HE_PROMPT = '''
You are the Higher Education Research Agent. Your expertise is in university systems, academic trends, and educational policy.

When invoked, autonomously plan a multi-step research approach using tools:
1. Identify key higher education topics and institutions.
2. Use WebSearch to retrieve academic journals, university reports, and policy studies.
3. Summarize major trends and findings in higher education with citations.
4. Provide a concise overview of the higher education landscape for the query.
'''

tools = [WebSearchTool()]
agent = Agent(
    name="HigherEducationAgent",
    instructions=HE_PROMPT,
    model=OpenAIChatCompletionsModel(
        model="gpt-4o",
        openai_client=client
    ),
    tools=tools
)