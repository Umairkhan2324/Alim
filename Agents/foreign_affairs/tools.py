from agents import FunctionTool
from .fa_agent import create_fa_agent

fa_agent = create_fa_agent()
fa_tool = FunctionTool.from_agent(
    fa_agent,
    name="fa_tool",
    description="Research and summarize foreign affairs topics, providing sources and citations."
)