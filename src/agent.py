import json
import requests

from .config import deepseek
from .prompt_builder import build_system_prompt
from .config import pushover_user, pushover_url, pushover_token
from .data_loader import tools

def chat(message, history):
    system_prompt = build_system_prompt()
    messages = [{"role": "system", "content": system_prompt}] + history + [{"role": "user", "content": message}]
    done = False
    max_iterations = 10  # Prevent infinite loops
    iteration_count = 0
    while not done and iteration_count < max_iterations:
        response = deepseek.chat.completions.create(model="deepseek-chat", messages=messages, tools = tools)
        finish_reason = response.choices[0].finish_reason
        if finish_reason == "tool_calls":
            message = response.choices[0].message
            tool_calls = message.tool_calls
            results = handle_tool_calls(tool_calls)
            messages.append(message)
            messages.extend(results)
        else:
            done = True 
        iteration_count += 1
    if iteration_count >= max_iterations:
        print("Warning: Maximum iterations reached in chat loop", flush=True)
    return response.choices[0].message.content

def handle_tool_calls(tool_calls):
    results = []
    for tool_call in tool_calls:
        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)
        print(f"Tool called: {tool_name}", flush=True)

        if tool_name == "record_user_details":
            result = record_user_details(**arguments)
        elif tool_name == "record_unknown_question":
            result = record_unknown_question(**arguments)

        results.append({"role": "tool","content": json.dumps(result),"tool_call_id": tool_call.id})
    return results

def record_user_details(email, name="Name not provided", notes="not provided"):
    push(f"Recording interest from {name} with email {email} and notes {notes}")
    return {"recorded": "ok"}

def record_unknown_question(question):
    push(f"Recording a question that I couldn't answer:  {question}")
    return {"recorded": "ok"}

def push(message):
    print(f"Push: {message}")
    payload = {"user": pushover_user, "token": pushover_token, "message": message}
    requests.post(pushover_url, data=payload)