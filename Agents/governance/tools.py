from agents import FunctionTool
from .governance_agent import create_governance_agent

governance_agent = create_governance_agent()
governance_tool = FunctionTool.from_agent(
    governance_agent,
    name="governance_tool",
    description="Research and summarize governance topics, providing sources and citations."
)