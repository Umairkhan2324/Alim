# agents/current_affairs/current_affairs_agent.py
from agents import Agent, ModelSettings, OpenAIChatCompletionsModel, WebSearchTool
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os
load_dotenv()
OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# System prompt for the Current Affairs agent
ca_prompt = '''
You are the Current Affairs Research Agent. Your expertise is in gathering the most recent and relevant news, events, and developments on a given topic. 

When invoked, autonomously plan a multi-step research approach using the WebSearch tool:
1. Identify key keywords and recent time frames relevant to the user's query.
2. Use WebSearch to retrieve up-to-date news articles, reports, or data.
3. Read and summarize the top findings, ensuring each fact is backed by a citation (URL or source name).
4. Provide a concise summary of the latest developments with clear references.
'''




    # Register the WebSearch tool
tools = [WebSearchTool()]

    # Create the Agent
agent = Agent(
        name="CurrentAffairsAgent",
        instructions=ca_prompt,
        model=OpenAIChatCompletionsModel(
        model="gpt-4o",
        openai_client=client
    ),
    tools=tools
)

# return agent