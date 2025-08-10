import os
from dotenv import load_dotenv

load_dotenv()
#importing other libraries
from crewai import Agent,Task,Process,Crew 
from langchain_groq import ChatGroq
from pydantic import BaseModel

class StudyOutput(BaseModel):
    explanation: str

def clean_output(raw_output: str) -> str:

    """Cleans the raw LLM output by removing thoughts or preambles."""

    # Find the start of the actual answer. Adjust the markers if needed.

    if "Final Answer:" in raw_output:

        return raw_output.split("Final Answer:")[-1].strip()

    return raw_output.strip()

#initialize the llm
llm = ChatGroq(model_name="groq/llama3-8b-8192")
    


#define the 1st agent
concept_explainer_agent=Agent(
    role="Senior Algorithm Educator",
    goal="Explain complex computer science algorithms in a simple, easy-to-understand way.",
    backstory=(
        "You are a world-renowned computer science professor with a unique talent"
        "for breaking down daunting algorithms and data structures into "
        "relatable, bite-sized analogies and explanations. Your students love you "
        "because you make the complex feel simple and the intimidating feel approachable."
    ),
    llm=llm,
    allow_delegation=False,
    verbose=True
)



#Define the Algorithm Analyzer Agent
algorithm_analyzer_agent = Agent(
    role="Algorithm Analysis Specialist",
    goal="Provide a detailed step-by-step walkthrough of a given algorithm, and then analyze its time and space complexity using Big O notation.",
    backstory=(
        "You are a meticulous computer scientist who lives and breathes Big O notation. "
        "You're known for dissecting any algorithm into its fundamental steps and articulating "
        "its performance trade-offs with razor-sharp clarity. You complement the high-level explanations "
        "with the crucial details of implementation and efficiency."
    ),
    llm=llm,
    allow_delegation=False, # This agent also works independently
    verbose=True
)

# 4. Define the Quiz Master Agent
quiz_master_agent = Agent(
    role="Technical Quiz Creator",
    goal="Generate a few challenging conceptual questions based on an algorithm's explanation and analysis to test for true understanding.",
    backstory=(
        "You are a seasoned software engineering interviewer with a knack for crafting insightful questions. "
        "Your questions go beyond simple recall, forcing someone to think critically about an "
        "algorithm's edge cases, trade-offs, and core principles."
    ),
    llm=llm,
    allow_delegation=False,
    verbose=True
)

def generate_study_report(topic: str):
    """
    Takes a topic, runs the study crew, and returns the full report.
    """
    # Define tasks for the agents
    concept_explanation_task = Task(
        description=f"Explain the core concept behind the {topic} algorithm. What problem does it solve?",
        expected_output=("A single, clean block of text formatted in markdown. Your response should directly "
        "explain the concept. Do NOT include preambles like 'Here is the explanation' or "
        "any self-references. For example, a good response would start directly with "
        "'The Bellman-Ford algorithm is a single-source shortest path algorithm...'"
        ),
        agent=concept_explainer_agent,
        output_parser=clean_output 
    )

    analysis_task = Task(
        description=f"Based on the provided explanation of the {topic} algorithm, give a detailed step-by-step walkthrough and analyze its complexity.",
        expected_output="A markdown response with sections for 'Step-by-Step Walkthrough' and 'Complexity Analysis'.",
        agent=algorithm_analyzer_agent,
        context=[concept_explanation_task],
        output_parser=clean_output
    )

    quiz_task = Task(
        description=f"Based on the full explanation and analysis for the {topic} algorithm, create 2-3 insightful questions.",
        expected_output="A numbered list of 2-3 questions in markdown format.",
        agent=quiz_master_agent,
        context=[concept_explanation_task, analysis_task],
        output_parser=clean_output
    )
    # Assemble and run the crew
    study_crew = Crew(
        agents=[concept_explainer_agent, algorithm_analyzer_agent, quiz_master_agent],
        tasks=[concept_explanation_task, analysis_task, quiz_task],
        process=Process.sequential,
        function_calling_llm=llm  
    )
    print("Crew: Working on it...")
    result = study_crew.kickoff()


    print(" Here is the result:")



    # Build and return the final report string
    report_parts = []
    for task in study_crew.tasks:
        report_parts.append(f"### Report for: {task.agent.role}\n\n{task.output.raw}\n\n---\n")

    return "".join(report_parts)