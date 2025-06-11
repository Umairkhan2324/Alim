from agents import FunctionTool
from .he_agent import create_he_agent

he_agent = create_he_agent()
he_tool = FunctionTool.from_agent(
    he_agent,
    name="higher_education_tool",
    description="Research and summarize higher education topics, providing sources and citations."
)