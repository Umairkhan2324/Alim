from agents import Agent, ChatOpenAI, ModelSettings, WebSearchTool

SYSTEM_PROMPT = '''
You are the Economics Research Agent. Your expertise is in macro and micro economic analysis, policy impacts, and economic data.

When invoked, autonomously plan a multi-step research approach using tools:
1. Identify relevant economic indicators and policy terms.
2. Use WebSearch to retrieve data reports, economic forecasts, and policy analyses.
3. Summarize key findings with citations.
4. Provide a concise economic analysis of the topic.
'''

def create_economics_agent():
    llm = ChatOpenAI(
        model="gpt-4o"
    )
    tools = [WebSearchTool()]
    agent = Agent(
        name="EconomicsAgent",
        system_prompt=SYSTEM_PROMPT,
        model=llm,
        tools=tools,
        settings=ModelSettings(
            temperature=0.0,
            parallel_tool_calls=False
        )
    )
    return agent