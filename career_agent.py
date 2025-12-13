from dotenv import load_dotenv
from agents import Agent, Runner, function_tool

load_dotenv()

@function_tool
def get_cv_info(saction: str) -> str:

    cv_data = {
        "experience": "Mechatronics Engineer at PAZUR (2005-present). Software Developer at TeamDev (2024-2025): Python, React, FastAPI.",
        "skills": "Programming: Python, JavaScript, React, FastAPI. Automation: n8n, Modbus. AI/ML: OpenAI API, Google Gemini, LangChain. Other: Docker, Git, PostgreSQL.",
        "education": "Mechatronics Engineering degree. Online courses: AI, Machine Learning, Web Development.",
        "projects": "AI Agents Course (30 lessons). n8n Automation Course on Udemy (EN, ES) and eduj.pl (PL).",
        "contact": "Email: pawelzarebski7@wp.pl, GitHub: github.com/pawelzarebski7"
    }
    
    section_lower = saction.lower()
    if section_lower in cv_data:
        return cv_data[section_lower]
    else:
        return "Section not found in CV. Available sections: experience, skills, education, projects, contact."

agent = Agent(
    name= "Career Agent",
    instructions="""You are a career assistant representing a job candidate.
    ALWAYS use the get_cv_info tool to answer questions about the candidate.
    - For questions about programming languages or technical skills: use get_cv_info('skills')
    - For questions about work history or experience: use get_cv_info('experience')
    - For questions about education: use get_cv_info('education')
    - For questions about projects: use get_cv_info('projects')
    Never say you don't have information - always use the tool first!""",
    tools=[get_cv_info]
)

questions = [
    "What programming languages do you know?",
    "Tell me about your work experience"
]

for question in questions:
    print(f"Question: {question}")
    result = Runner.run_sync(agent, question)
    print(f"Answer: {result.final_output}\n")
    print("-----\n")