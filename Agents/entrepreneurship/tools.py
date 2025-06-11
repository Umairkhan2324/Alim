from agents import FunctionTool
from .ent_agent import create_entrepreneurship_agent

ent_agent = create_entrepreneurship_agent()
ent_tool = FunctionTool.from_agent(
    ent_agent,
    name="entrepreneurship_tool",
    description="Research and summarize entrepreneurship topics, providing sources and citations."
)