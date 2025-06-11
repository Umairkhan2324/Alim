from agents import FunctionTool
from .finance_agent import create_finance_agent

finance_agent = create_finance_agent()
finance_tool = FunctionTool.from_agent(
    finance_agent,
    name="finance_tool",
    description="Research and summarize finance topics, providing sources and citations."
)