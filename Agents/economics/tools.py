from agents import FunctionTool
from .economics_agent import agent

# Wrap the agent as a FunctionTool for the Orchestrator to call
economics_tool = agent.as_tool(
    tool_name="economics_tool",
    tool_description="Explains complex economic concepts and provides economic forecasts and analysis."
)