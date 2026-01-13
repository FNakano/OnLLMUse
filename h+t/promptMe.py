from ollama import chat
# This is a merge between tooltest.py and mycontinuousprompt.py

def get_temperature(city: str) -> str:
  """Get the current temperature for a city
  
  Args:
    city: The name of the city

  Returns:
    The current temperature for the city
  """
  temperatures = {
    "New York": "22°C",
    "London": "15°C",
    "São Paulo":"25",
    "Tokyo": "18°C",
    "Amsterdam":"10",
  }
  print (city)
  return temperatures.get(city, "Unknown")

def get_current_time() -> dict:
    """Get the current date and time.
    Returns:
        dict: Current time information with status and message
    """
    now = datetime.now()
    time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    day_str = now.strftime("%A")
    return {
        "status": "success",
        "time": time_str,
        "day": day_str,
        "message": f"Current time is {time_str} ({day_str})"
    }

from ollama import chat

import json

from datetime import datetime

global messages

# Initial system prompt to guide the model's behavior
messages_setup = [
    {
        'role': 'system',
        'content': 'You are a helpful assistant that remembers previous questions.'
    }
]

def chat_with_ollama(prompt):
  # messages=messages_setup # uncomment to disable response history
  # Append the user's new message to the history
  messages.append({'role': 'user', 'content': prompt})
    
  # Send the *entire* accumulated messages list to the API
  # pass functions directly as tools in the tools list or as a JSON schema
  response = chat(model="qwen3", messages=messages, tools=[get_temperature, get_current_time], think=True, keep_alive=-1)
  # keeps model loaded indefinitely - https://docs.ollama.com/faq#how-do-i-keep-a-model-loaded-in-memory-or-make-it-unload-immediately
  
  if response.message.tool_calls:
    # only recommended for models which only return a single tool call
    call = response.message.tool_calls[0]
    print (call)
    print (call.function.arguments)
    if (call.function.name=='get_temperature') : result = get_temperature(**call.function.arguments)
    if (call.function.name=='get_current_time') : result = get_current_time(**call.function.arguments)
    print (result)
    # add the tool result to the messages
    messages.append({"role": "tool", "tool_name": call.function.name, "content": str(result)})  # a third person in the chat...
    response = chat(model="qwen3", messages=messages, tools=[get_temperature, get_current_time], think=True, keep_alive=-1)
    # Append the model's response to the history for the next turn
    messages.append({'role': 'assistant', 'content': response['message']['content']})
  
  return response['message']['content']


def get_history (filename):
  global messages
  try:
    with open ('history.json', 'r') as file:
      messages=json.load(file)
      print (messages)
  except FileNotFoundError:
    print('Did not find file named history.json, starting from empty history.')


messages=messages_setup
get_history('history.json')
# print (messages)
while True:
  try:
    q=input()
  except (EOFError, KeyboardInterrupt):
    print ('Terminating conversation loop.')
    break
  response1 = chat_with_ollama(q)
  print(f"AI: {response1}\n")

with open('history.json', 'w') as file:
  json.dump(messages, file)
# end

