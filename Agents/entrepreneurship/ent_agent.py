from agents import Agent, ChatOpenAI, ModelSettings, WebSearchTool

SYSTEM_PROMPT = '''
You are the Entrepreneurship Research Agent. Your expertise is in startups, business models, and market entry strategies.

When invoked, autonomously plan a multi-step research approach using tools:
1. Identify key startup and entrepreneurship terms.
2. Use WebSearch to retrieve case studies, market analyses, and startup data.
3. Summarize critical findings with citations.
4. Provide a concise entrepreneurship overview for the topic.
'''

def create_entrepreneurship_agent():
    llm = ChatOpenAI(
        model="gpt-4o"
    )
    tools = [WebSearchTool()]
    agent = Agent(
        name="EntrepreneurshipAgent",
        system_prompt=SYSTEM_PROMPT,
        model=llm,
        tools=tools,
        settings=ModelSettings(
            temperature=0.0,
            parallel_tool_calls=False
        )
    )
    return agent