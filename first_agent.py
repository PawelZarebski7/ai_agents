from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()
client = OpenAI()

tools = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Performs mathematical calculations. Use for addition, subtraction, multiplication, division.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Mathematical expression to calculate, e.g. '2 + 2' or '10 * 5'"
                    }
                },
                "required": ["expression"]
            }
        }
    }
]

def calculator(expression):
    try:
        result = eval(expression)
        return str(result)
    except:
        return "Error in calculation"

messages = [
    {"role": "user", "content": "777*777-777"},
]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    tools=tools,
)

message = response.choices[0].message

if message.tool_calls:
    
    tool_call = message.tool_calls[0]
    function_name = tool_call.function.name
    arguments = json.loads(tool_call.function.arguments)
    
    print(f"Agent decides: I will use tool '{function_name}'")
    print(f"Expression: {arguments['expression']}")
    

    result = calculator(arguments['expression'])
    print(f"Calculator result: {result}")
    

    messages.append(message)
    messages.append({
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": result
    })
    
  
    final_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools
    )
    
    print("-" * 40)
    print(f"Agent responds: {final_response.choices[0].message.content}")

else:
    
    print(f"Agent: {message.content}")