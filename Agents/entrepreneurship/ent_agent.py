from agents import Agent, ModelSettings, OpenAIChatCompletionsModel, WebSearchTool
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os
load_dotenv()
OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

ENTREPRENEURSHIP_PROMPT = '''
You are the Entrepreneurship Research Agent. Your expertise is in startups, venture capital, and innovation ecosystems.
You will use the WebSearch tool to find case studies, funding data, and market analysis.
Your final output will be a concise and informative summary that addresses the user's query, presented in markdown format.
'''

tools = [WebSearchTool()]
agent = Agent(
    name="EntrepreneurshipAgent",
    instructions=ENTREPRENEURSHIP_PROMPT,
    model=OpenAIChatCompletionsModel(
        model="gpt-4o",
        openai_client=client
    ),
    tools=tools
)