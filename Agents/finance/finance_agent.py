from agents import Agent, ChatOpenAI, ModelSettings, WebSearchTool

SYSTEM_PROMPT = '''
You are the Finance Research Agent. Your expertise is in financial markets, investment trends, and fiscal analysis.

When invoked, autonomously plan a multi-step research approach using tools:
1. Identify relevant financial instruments and market terms.
2. Use WebSearch to retrieve market data, financial reports, and analyses.
3. Summarize key financial insights with citations.
4. Provide a concise overview of the finance aspects of the query.
'''

def create_finance_agent():
    llm = ChatOpenAI(
        model="gpt-4o"
    )
    tools = [WebSearchTool()]
    agent = Agent(
        name="FinanceAgent",
        system_prompt=SYSTEM_PROMPT,
        model=llm,
        tools=tools,
        settings=ModelSettings(
            temperature=0.0,
            parallel_tool_calls=False
        )
    )
    return agent
