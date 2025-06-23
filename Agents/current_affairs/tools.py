from .current_affairs_agent import agent

# Wrap the agent as a FunctionTool for the Orchestrator to call
current_affairs_tool = agent.as_tool(
    tool_name="current_affairs_tool",
    tool_description="Research and summarize the latest news and developments on a topic, providing sources and citations."
)