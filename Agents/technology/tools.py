from .tech_agent import agent

technology_tool = agent.as_tool(
    tool_name="technology_tool",
    tool_description="Explains emerging technologies, software development, and AI advancements."
)