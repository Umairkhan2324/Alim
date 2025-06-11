from agents import Agent, ChatOpenAI, ModelSettings, WebSearchTool

SYSTEM_PROMPT = '''
You are the Innovation Research Agent. Your expertise is in R&D, patents, and emerging innovation trends.

When invoked, autonomously plan a multi-step research approach using tools:
1. Identify key innovation and patent terms.
2. Use WebSearch to retrieve patent databases, R&D reports, and innovation indices.
3. Summarize major innovation findings with citations.
4. Provide a concise innovation overview for the query.
'''

def create_innovation_agent():
    llm = ChatOpenAI(
        model="gpt-4o"
    )
    tools = [WebSearchTool()]
    agent = Agent(
        name="InnovationAgent",
        system_prompt=SYSTEM_PROMPT,
        model=llm,
        tools=tools,
        settings=ModelSettings(
            temperature=0.0,
            parallel_tool_calls=False
        )
    )
    return agent