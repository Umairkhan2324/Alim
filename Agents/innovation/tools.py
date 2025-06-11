from agents import FunctionTool
from .innovation_agent import create_innovation_agent

innovation_agent = create_innovation_agent()
innovation_tool = FunctionTool.from_agent(
    innovation_agent,
    name="innovation_tool",
    description="Research and summarize innovation topics, providing sources and citations."
)