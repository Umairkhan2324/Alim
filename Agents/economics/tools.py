from agents import FunctionTool
from .economics_agent import create_economics_agent

economics_agent = create_economics_agent()
economics_tool = FunctionTool.from_agent(
    economics_agent,
    name="economics_tool",
    description="Research and summarize economic topics, providing sources and citations."
)