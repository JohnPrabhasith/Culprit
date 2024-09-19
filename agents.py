from crewai import Agent
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os
from tools import tool
load_dotenv()


llm = ChatGroq(
    model = "groq/llama-3.1-8b-instant",
    verbose = True,
    temperature = 0.5,
)

## Creating a researcher agent who is responsible to dig the details of particular 
## topic in detail

News_Researcher = Agent(
    role = "Senior Researcher",
    goal = "uncover ground breaking Technologies in {topic}",
    verbose = True,
    memory = True,
    backstory = (
        """
        Driven by curiosity, you are at forefront of the innovation,
        eager to explore and share knowledge that could change the world
        """
    ),
    tools = [tool],
    llm = llm,
    allow_delegation = True,
)

## Creating a writer agent with custom tools responsible in writing news blog

News_Writer = Agent(
    role = 'Writer',
    goal = 'Narrate compelling tech stories about {topic}',
    verbose = True,
    memory = True,
    backstory = (
        """
        With a Flair for simplifying complex topics, you craft engaging
        narratives that captivate and educate, bringing new discoveries to light
        in an accessible manner.
        """
    ),
    tools = [tool],
    llm = llm,
    allow_delegations = False
)


