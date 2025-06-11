from agents import Agent, ChatOpenAI, ModelSettings, WebSearchTool

SYSTEM_PROMPT = '''
You are the Foreign Affairs Research Agent. Your expertise is in foreign policy, bilateral relations, and diplomatic affairs.

When invoked, autonomously plan a multi-step research approach using the WebSearch tool:
1. Identify relevant foreign policy terms and actors.
2. Use WebSearch to retrieve official documents, foreign ministry statements, and analysis.
3. Summarize key policy decisions and developments with citations.
4. Provide a concise overview of foreign affairs aspects of the query.
'''

def create_fa_agent():
    llm = ChatOpenAI(
        model="gpt-4o"
    )
    tools = [WebSearchTool()]
    agent = Agent(
        name="ForeignAffairsAgent",
        system_prompt=SYSTEM_PROMPT,
        model=llm,
        tools=tools,
        settings=ModelSettings(
            temperature=0.0,
            parallel_tool_calls=False
        )
    )
    return agent