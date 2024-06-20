from crewai import Crew
from agents import planner, Writer, editor
from tasks import plan, write, edit

# Initialize Crew
crew = Crew(
    agents=[planner, Writer, editor],
    tasks=[plan, write, edit],
    verbose=2
)

def generate_workflow(topic, tone, word_count):
    result = crew.kickoff(inputs={"topic": topic, "tone": tone, "word_count": word_count})
    return result
