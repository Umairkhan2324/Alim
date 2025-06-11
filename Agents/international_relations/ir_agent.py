from agents import Agent, ChatOpenAI, ModelSettings, WebSearchTool

SYSTEM_PROMPT = '''
You are the International Relations Research Agent. Your expertise is in analyzing diplomatic, geopolitical, and global policy developments.

When invoked, autonomously plan a multi-step research approach using the WebSearch tool:
1. Identify key diplomatic or geopolitical terms relevant to the user's query.
2. Use WebSearch to retrieve authoritative news, think-tank reports, and official statements.
3. Summarize the most relevant insights with citations (URL or source name).
4. Provide a concise, structured analysis of international relations aspects of the topic.
'''

def create_ir_agent():
    llm = ChatOpenAI(
        model="gpt-4o"
    )
    tools = [WebSearchTool()]
    agent = Agent(
        name="IRAgent",
        system_prompt=SYSTEM_PROMPT,
        model=llm,
        tools=tools,
        settings=ModelSettings(
            temperature=0.0,
            parallel_tool_calls=False
        )
    )
    return agent