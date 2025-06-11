from agents import FunctionTool, Agent
from .current_affairs_agent import create_current_affairs_agent

# Instantiate the Current Affairs agent
tagent = create_current_affairs_agent()

# Wrap the agent as a FunctionTool for the Orchestrator to call
current_affairs_tool = FunctionTool.from_agent(
    Agent,
    name="current_affairs_tool",
    description="Research and summarize the latest news and developments on a topic, providing sources and citations."
)
