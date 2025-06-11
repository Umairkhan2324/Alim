from agents import FunctionTool
from .governance_agent import agent


governance_tool = agent.as_tool(
    tool_name="governance_tool",
    tool_description="Explains governance models, public policy, and organizational structures."
)