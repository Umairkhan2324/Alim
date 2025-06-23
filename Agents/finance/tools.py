from .finance_agent import agent

finance_tool = agent.as_tool(
    tool_name="finance_tool",
    tool_description="Delivers financial analysis, investment strategies, and market insights."
)