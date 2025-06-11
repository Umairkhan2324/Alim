from agents import FunctionTool
from .ir_agent import agent

ir_tool = agent.as_tool(
    tool_name="ir_tool",
    tool_description="Analyzes international relations, global security, and geopolitical dynamics."
)