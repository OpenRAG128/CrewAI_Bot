from crewai import Crew
from agents import planner, Writer, editor
from tasks import plan, write, edit
from IPython.display import Markdown

crew = Crew(
    agents=[planner, Writer, editor],
    tasks=[plan, write, edit],
    verbose=2
)

result = crew.kickoff(inputs={"topic":"Artificial Intelligence"})

Markdown(result)