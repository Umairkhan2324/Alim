from agents import FunctionTool
from .current_affairs_agent import agent

# Instantiate the Current Affairs agent
# agent = create_current_affairs_agent()

# Wrap the agent as a FunctionTool for the Orchestrator to call
# @FunctionTool(
#     agent,
#     name="current_affairs_tool",
#     description="Research and summarize the latest news and developments on a topic, providing sources and citations."
# )
current_affairs_tool = agent.as_tool(
    tool_name="current_affairs_tool",
    tool_description="Research and summarize the latest news and developments on a topic, providing sources and citations."
)