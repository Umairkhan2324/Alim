# agents/commerce/tools.py
from agents import FunctionTool
from .commerce_agent import create_commerce_agent

# Instantiate the Commerce agent
commerce_agent = create_commerce_agent()

# Wrap the agent as a FunctionTool for the Orchestrator to call
commerce_tool = FunctionTool.from_agent(
    commerce_agent,
    name="commerce_tool",
    description="Research and summarize commerce topics (trade, retail, e-commerce, market data), providing sources and citations."
)