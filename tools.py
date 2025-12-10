from dotenv import load_dotenv
from agents import Agent, Runner, function_tool
import random

load_dotenv()

@function_tool
def calculator(expression: str) -> str:
    try:
        result = str(eval(expression))
    except:
        result = "Error in calculation"

@function_tool
def random_number(min_value: int, max_value: int) -> str:
    number = random.randint(min_value, max_value)
    return str(number)

@function_tool
def analyze_text(text: str) -> str:
    chars = len(text)
    words = len(text.split())
    senentences = text.count('.') + text.count('!') + text.count('?')
    return f"Characters: {chars}, Words: {words}, Sentences: {senentences}"

agent = Agent(
    name="MultiToolAgent",
    instructions="You are helpful assistant. Use appropriate tool for each task.",
    tools=[calculator, random_number, analyze_text]
)

questions = [
    "What is 1234 * 5678?",
    "Generate a random number between 1 and 100.",
    "Analyze the following text: 'Hello world! This is a test. How many words"
]

for question in questions:
    print(f"Question: {question}")
    result = Runner.run_sync(agent, question)
    print(f"Answer: {result.final_output}\n")