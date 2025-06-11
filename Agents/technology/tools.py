from agents import FunctionTool
from .tech_agent import create_technology_agent

technology_agent = create_technology_agent()
technology_tool = FunctionTool.from_agent(
    technology_agent,
    name="technology_tool",
    description="Research and summarize technology topics, providing sources and citations."
)