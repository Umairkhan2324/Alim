from agents import FunctionTool
from .ent_agent import agent


entrepreneurship_tool = agent.as_tool(
    tool_name="entrepreneurship_tool",
    tool_description="Provides guidance on starting and growing a business, from ideation to execution."
)