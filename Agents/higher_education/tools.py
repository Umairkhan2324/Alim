from .he_agent import agent

higher_education_tool = agent.as_tool(
    tool_name="higher_education_tool",
    tool_description="Covers trends in higher education, university policies, and academic research."
)