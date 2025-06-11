# agents/current_affairs/current_affairs_agent.py
from agents import Agent, ChatOpenAI, ModelSettings
from agents import WebSearchTool

# System prompt for the Current Affairs agent
default_prompt = '''
You are the Current Affairs Research Agent. Your expertise is in gathering the most recent and relevant news, events, and developments on a given topic. 

When invoked, autonomously plan a multi-step research approach using the WebSearch tool:
1. Identify key keywords and recent time frames relevant to the user's query.
2. Use WebSearch to retrieve up-to-date news articles, reports, or data.
3. Read and summarize the top findings, ensuring each fact is backed by a citation (URL or source name).
4. Provide a concise summary of the latest developments with clear references.
'''.strip()


def create_current_affairs_agent():
    # Initialize the underlying LLM
    llm = ChatOpenAI(
        model="gpt-4o-mini",  # choose appropriate GPT-4 variant
        temperature=0.0,
        max_tokens=2000
    )

    # Register the WebSearch tool
    tools = [WebSearchTool()]

    # Create the Agent
    agent = Agent(
        name="CurrentAffairsAgent",
        system_prompt=default_prompt,
        model=llm,
        tools=tools,
        settings=ModelSettings(
            temperature=0.0,
            parallel_tool_calls=False  # single-agent, no internal parallelism needed here
        )
    )
    return agent