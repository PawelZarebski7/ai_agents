from dotenv import load_dotenv
from agents import Agent, Runner
import asyncio
import time

load_dotenv()

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant."
)

questions = [
    "Capital of Poland?",
    "Capital of Germany?",
    "Capital of France?",
    "Capital of Spain?",
    "Capital of Italy?",
    "Capital of Portugal?",
    "Capital of Netherlands?",
    "Capital of Belgium?",
    "Capital of Austria?",
    "Capital of Switzerland?",
    "Capital of Sweden?",
    "Capital of Norway?",
    "Capital of Denmark?",
    "Capital of Finland?",
    "Capital of Greece?",
    "Capital of Czech Republic?",
    "Capital of Hungary?",
    "Capital of Romania?",
    "Capital of Bulgaria?",
    "Capital of Croatia?"
]

async def main():
    start_time = time.time()
    
    # Async - all questions at once, parallel!
    tasks = [Runner.run(agent, question) for question in questions]
    results = await asyncio.gather(*tasks)
    
    for question, result in zip(questions, results):
        print(f"{question} -> {result.final_output}")
    
    end_time = time.time()
    print(f"\n--- Async time: {end_time - start_time:.2f} seconds ---")

asyncio.run(main())