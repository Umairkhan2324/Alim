from agents import Agent, ChatOpenAI, ModelSettings, WebSearchTool

SYSTEM_PROMPT = '''
You are the Higher Education Research Agent. Your expertise is in academic trends, university policies, and education metrics.

When invoked, autonomously plan a multi-step research approach using tools:
1. Identify key education policy and academic terms.
2. Use WebSearch to retrieve academic papers, university reports, and statistics.
3. Summarize key educational insights with citations.
4. Provide a concise higher education overview for the query.
'''

def create_he_agent():
    llm = ChatOpenAI(
        model="gpt-4o"
    )
    tools = [WebSearchTool()]
    agent = Agent(
        name="HigherEducationAgent",
        system_prompt=SYSTEM_PROMPT,
        model=llm,
        tools=tools,
        settings=ModelSettings(
            temperature=0.0,
            parallel_tool_calls=False
        )
    )
    return agent