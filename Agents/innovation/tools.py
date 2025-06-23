from .innovation_agent import agent

innovation_tool = agent.as_tool(
    tool_name="innovation_tool",
    tool_description="Tracks technological breakthroughs, R&D, and disruptive innovations."
)