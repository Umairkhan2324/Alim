from agents import FunctionTool
from .ir_agent import create_ir_agent

ir_agent = create_ir_agent()
ir_tool = FunctionTool.from_agent(
    ir_agent,
    name="ir_tool",
    description="Research and summarize international relations topics, providing sources and citations."
)