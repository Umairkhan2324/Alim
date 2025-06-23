# agents/commerce/tools.py
from .commerce_agent import agent

# Wrap the agent as a FunctionTool for the Orchestrator to call
commerce_tool = agent.as_tool(
    tool_name="commerce_tool",
    tool_description="Analyzes commerce, trade, and business trends, providing data-driven insights."
)