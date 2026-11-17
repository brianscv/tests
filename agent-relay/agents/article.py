from agents import Agent, Runner, WebSearchTool
from pydantic import BaseModel


class Plan(BaseModel):
    outline: list[str]
    summary: str


researcher = Agent(
    name="researcher",
    instructions="Collect facts about the topic from the web.",
    tools=[WebSearchTool()],
)
writer = Agent(name="writer", instructions="Write an article from the notes you are given.")
planner = Agent(
    name="planner",
    instructions="Plan an article about the topic.",
    output_type=Plan,
)


async def write_article(topic: str) -> str:
    research = await Runner.run(researcher, topic)
    article = await Runner.run(writer, research.final_output)
    return article.final_output


async def write_planned(topic: str) -> str:
    plan = await Runner.run(planner, topic)
    article = await Runner.run(writer, plan.final_output.summary)
    return article.final_output
