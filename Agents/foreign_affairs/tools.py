from .fa_agent import agent

fa_tool = agent.as_tool(
    tool_name="fa_tool",
    tool_description="Provides analysis on foreign policy, international relations, and diplomatic strategies."
)