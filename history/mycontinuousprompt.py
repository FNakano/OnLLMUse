from ollama import chat

import json

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
    response = chat(model='gemma3', messages=messages)
    
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
print (messages)
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
