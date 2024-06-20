from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq

llm=ChatGroq(temperature=0,
             model_name="llama3-70b-8192",
             api_key="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")

planner = Agent(
    llm=llm,
    role="Content Planner",
    goal="Plan engaging and long factual content on {topic}",
    backstory="You are wokring on planning a blog article"
    "about the topic: {topic}."
    "you collect information that helps the"
    "audience learn something"
    "and make informed decisions"
    "your work is the basis for"
    "the content writer to write an article on this topic.",
    allow_delegation=False,
    verbose=True
)

Writer=Agent(
    llm=llm,
    role="Content Writer",
    goal="write insightful and factually accurate"
    "opinion piece about the topic: {topic}",
    backstory="You're working on a writing"
    "a new opinion piece about the topic: {topic}"
    "you base your writing on the work of"
    "the content planner, who provides an outline"
    "and relevant context about the topic"
    "You follow the main objectives and"
    "direction of the outline"
    "as provided by the content planner. ",
    allow_delegation=False,
    verbose=True
)

editor = Agent(
    llm=llm,    
    role="Editor",
    goal="Edit a given blog post to align with "
         "the writing style of the organization. ",
    backstory="You are an editor who receives a blog post "
              "from the Content Writer. "
              "Your goal is to review the blog post "
              "to ensure that it follows journalistic best practices,"
              "provides balanced viewpoints "
              "when providing opinions or assertions, "
              "and also avoids major controversial topics "
              "or opinions when possible.",
    allow_delegation=False,
    verbose=True
)




