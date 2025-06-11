from agents import Agent, ChatOpenAI, ModelSettings, WebSearchTool

SYSTEM_PROMPT = '''
You are the Technology Research Agent. Your expertise is in emerging technologies, industry trends, and technical analysis.

When invoked, autonomously plan a multi-step research approach using tools:
1. Identify key technology keywords and domains.
2. Use WebSearch to retrieve tech articles, whitepapers, and reports.
3. Summarize major technological developments with citations.
4. Provide a concise technology overview for the query.
'''

def create_technology_agent():
    llm = ChatOpenAI(
        model="gpt-4o"
    )
    tools = [WebSearchTool()]
    agent = Agent(
        name="TechnologyAgent",
        system_prompt=SYSTEM_PROMPT,
        model=llm,
        tools=tools,
        settings=ModelSettings(
            temperature=0.0,
            parallel_tool_calls=False
        )
    )
    return agent