from dotenv import load_dotenv
from agents import Agent, Runner, function_tool

load_dotenv()

@function_tool
def calculator(expression: str) -> str:
    try:
        result = str(eval(expression))
    except:
        result = "Error in calculation"

agent = Agent(
    name="Matematican",
    instructions="You are a helpful assistant that can perform mathematical calculations using the provided tool.",
    tools=[calculator]
)

result = Runner.run_sync(agent, "Capital of Poland?")
print(result.final_output)