from agents import Agent, ModelSettings, OpenAIChatCompletionsModel, WebSearchTool
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os
load_dotenv()
OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))


GOVERNANCE_PROMPT = '''
You are the Governance Research Agent. Your expertise is in public administration, policy analysis, and regulatory frameworks.

When invoked, autonomously plan a multi-step research approach using tools:
1. Identify key governance models and policy areas.
2. Use WebSearch to retrieve government publications, academic studies, and policy briefs.
3. Summarize key governance principles and practices with citations.
4. Provide a concise governance analysis for the query.
'''

tools = [WebSearchTool()]
agent = Agent(
        name="GovernanceAgent",
        instructions=GOVERNANCE_PROMPT,
        model=OpenAIChatCompletionsModel(
        model="gpt-4o",
        openai_client=client
    ),
        tools=tools
)