from agents import Agent, ChatOpenAI, ModelSettings, WebSearchTool

SYSTEM_PROMPT = '''
You are the Governance Research Agent. Your expertise is in public policy, regulation, and governance frameworks.

When invoked, autonomously plan a multi-step research approach using tools:
1. Identify key governance and regulatory terms.
2. Use WebSearch to retrieve policy papers, government reports, and analyses.
3. Summarize important policy insights with citations.
4. Provide a concise governance overview for the query.
'''

def create_governance_agent():
    llm = ChatOpenAI(
        model="gpt-4o"
    )
    tools = [WebSearchTool()]
    agent = Agent(
        name="GovernanceAgent",
        system_prompt=SYSTEM_PROMPT,
        model=llm,
        tools=tools,
        settings=ModelSettings(
            temperature=0.0,
            parallel_tool_calls=False
        )
    )
    return agent