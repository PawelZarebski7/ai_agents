from dotenv import load_dotenv
from agents import Agent, Runner

load_dotenv()

# ========================================
# AGENT 1: RESEARCHER
# Szuka informacji
# ========================================
researcher = Agent(
    name="Researcher",
    instructions="""You are an expert researcher.
    Your goal is to find accurate information about any topic.
    You present facts in clear bullet points.
    You are thorough and reliable."""
)

# ========================================
# AGENT 2: WRITER
# Pisze treść na podstawie informacji
# ========================================
writer = Agent(
    name="Writer",
    instructions="""You are a skilled content writer.
    Your goal is to write clear, engaging content.
    You take information and turn it into easy-to-read paragraphs.
    You use simple language that anyone can understand."""
)

# ========================================
# KROK 1: RESEARCHER SZUKA INFORMACJI
# ========================================
print("=" * 50)
print("STEP 1: RESEARCHER")
print("=" * 50)

research_result = Runner.run_sync(
    researcher, 
    "Research the topic: What is artificial intelligence? Give me key facts in bullet points."
)
print(research_result.final_output)

# ========================================
# KROK 2: WRITER PISZE NA PODSTAWIE RESEARCHU
# ========================================
print("\n")
print("=" * 50)
print("STEP 2: WRITER")
print("=" * 50)

writer_prompt = f"""Based on this research, write a short paragraph about AI:

{research_result.final_output}

Write 3-4 sentences that are easy to understand."""

write_result = Runner.run_sync(writer, writer_prompt)
print(write_result.final_output)

print("\n")
print("=" * 50)
print("Two agents working together!")
print("=" * 50)