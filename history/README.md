# history - Keeping chat history between sessions.

## Objective

Gain understanding about data persistence in LLMs, build (and test) data persistence.

## Introduction

Data persistence is about how something (a system, a program) retains data... how much data, for how long, ... Words like *context*, *stateful*/*stateless* are related to it.

As far as I tested, `ollama run gemma3` creates a LLM chat which retains message data during its execution. A single execution of `ollama run` is a *session*. If it is the first time you read `ollama run`, try refering to [Notes on LLM Use](https://github.com/FNakano/OnLLMUse)

In a session if you type in `Hi! My name is Fábio`, the model will keep this information and if you ask `What is my name?` it is going to answer `Your name is Fábio`. When LLM is called through its Python API `ollama.chat(...)` function, two chat calls are made. The first states `Hi! My name is Fábio` which is answered with a greeting and the second states `What is my name?`. If there is no message history, LLM won't answer `Your name is Fábio`.

Searching the web I found some discussions that made sense to me (I cannot say that these discussions are/are not complete, correct, ...) .

> The `genai` SDK supports stateful chat session, which makes it quite easy to test our example as we can easily append the different messages. First, we start with a simple greeting to see what Gemma does. (https://www.philschmid.de/gemma-function-calling)

Someone categorized data persistence in LLMs:

> The LLM does not inherently store conversation data. The application managing the LLM is responsible for handling conversation context within a session and optionally persisting important information across sessions using external storage mechanisms.
> (...)
> Large Language Models (LLMs) like those used in local applications (e.g., Ollama’s Gemma2) do not inherently retain conversation memory across separate sessions. Instead, they rely on the context provided within the current session to maintain a conversation’s continuity. Here’s how this typically works:
> 1. Session-Based Memory: ...
> 2. Context Window: ...
> 3. Temporary Storage: ...
> 4. Stateful Management: ...
> 5. Persistent Storage (Optional): ...
(https://www.reddit.com/r/ollama/comments/1edan5c/how_does_an_llm_retain_conversation_memory/ )

What I call *history* falls in Persistent Storage category. Depending on how it is implemented, it can serve as a human-readable log which can be searched and indexed even using the LLM.

Some more web searching made Google (Gemini) to present me an almost finished code:

```python
import ollama

# Initial system prompt to guide the model's behavior
messages = [
    {
        'role': 'system',
        'content': 'You are a helpful assistant that remembers previous questions.'
    }
]

def chat_with_ollama(prompt):
    # Append the user's new message to the history
    messages.append({'role': 'user', 'content': prompt})
    
    # Send the *entire* accumulated messages list to the API
    response = ollama.chat(model='gemma3', messages=messages)
    
    # Append the model's response to the history for the next turn
    messages.append({'role': 'assistant', 'content': response['message']['content']})
    
    return response['message']['content']

# Example conversation
print(f"User: What is the capital of France?")
response1 = chat_with_ollama("What is the capital of France?")
print(f"AI: {response1}\n")

print(f"User: What did I ask first?")
response2 = chat_with_ollama("What did I ask first?")
print(f"AI: {response2}\n")

print(f"User: How many people live there?")
response3 = chat_with_ollama("How many people live there?")
print(f"AI: {response3}\n")

```

I *just* need to add appropriate file reading and writing and a loop to chat to the LLM...

## Results

Complete script is in `mycontinuousprompt.py`. If this is your first script using Ollama, I recomend you to try its Python API quickstart example first (https://docs.ollama.com/quickstart#python)

`mycontinuousprompt.py` reads message history from file `history.json` (if the file exists) into the dict variable `messages`, configures and starts chatting. Each typed/generated message is appended to `messages`. The chat can be finished with either CTRL-C or CTRL-D. `messages` is written back to the file `history.json`.

### Inspection

`history.json` is the latest history written. It started with `history.bk` content and had some messages appended. Have a look at the files contents to see what messages were chatted.

#### history.bk listing

`history.bk` is a version previous to the test session.

```json
[
  {
    "role": "system",
    "content": "You are a helpful assistant that remembers previous questions."
  },
  {
    "role": "user",
    "content": "Hi, Gemma!"
  },
  {
    "role": "assistant",
    "content": "Hi there! It’s good to hear from you. How can I help you today? Do you want to chat, or do you have a specific question you’d like to ask?"
  },
  {
    "role": "user",
    "content": "I'm doing quick tests with the chat. Can you help me?"
  },
  {
    "role": "assistant",
    "content": "Absolutely! I’m happy to help with quick tests. What kind of tests are you running? Do you have a specific format in mind, or should we just start with some general questions? 😊"
  },
  {
    "role": "user",
    "content": "Great! Just keep some information: my name is Fábio and today is Jan, 9th, 2025, 10:20AM... Okay?!"
  },
  {
    "role": "assistant",
    "content": "Okay, Fábio! Got it. Just to confirm:\n\n*   **Name:** Fábio\n*   **Today’s Date:** January 9th, 2025\n*   **Time:** 10:20 AM\n\nPerfect! Let’s do these tests. What’s the first one?"
  },
  {
    "role": "user",
    "content": "I'm going to finish this session an start a new one..."
  },
  {
    "role": "assistant",
    "content": "Okay, Fábio! Sounds good. Let’s start a new session then. I’ve cleared my memory of our previous conversation. \n\nReady for a fresh start? What do you want to do now?"
  },
  {
    "role": "user",
    "content": "Bye!"
  },
  {
    "role": "assistant",
    "content": "Goodbye, Fábio! It was nice chatting with you. Feel free to start a new session anytime. 😊"
  }
]
```
(prettified with https://jsonformatter.org/)

#### history.json listing

`history.json` is a version after the test session.

```json
[
  {
    "role": "system",
    "content": "You are a helpful assistant that remembers previous questions."
  },
  {
    "role": "user",
    "content": "Hi, Gemma!"
  },
  {
    "role": "assistant",
    "content": "Hi there! It’s good to hear from you. How can I help you today? Do you want to chat, or do you have a specific question you’d like to ask?"
  },
  {
    "role": "user",
    "content": "I'm doing quick tests with the chat. Can you help me?"
  },
  {
    "role": "assistant",
    "content": "Absolutely! I’m happy to help with quick tests. What kind of tests are you running? Do you have a specific format in mind, or should we just start with some general questions? 😊"
  },
  {
    "role": "user",
    "content": "Great! Just keep some information: my name is Fábio and today is Jan, 9th, 2025, 10:20AM... Okay?!"
  },
  {
    "role": "assistant",
    "content": "Okay, Fábio! Got it. Just to confirm:\n\n*   **Name:** Fábio\n*   **Today’s Date:** January 9th, 2025\n*   **Time:** 10:20 AM\n\nPerfect! Let’s do these tests. What’s the first one?"
  },
  {
    "role": "user",
    "content": "I'm going to finish this session an start a new one..."
  },
  {
    "role": "assistant",
    "content": "Okay, Fábio! Sounds good. Let’s start a new session then. I’ve cleared my memory of our previous conversation. \n\nReady for a fresh start? What do you want to do now?"
  },
  {
    "role": "user",
    "content": "Bye!"
  },
  {
    "role": "assistant",
    "content": "Goodbye, Fábio! It was nice chatting with you. Feel free to start a new session anytime. 😊"
  },
  {
    "role": "user",
    "content": "Hello, Gemma!"
  },
  {
    "role": "assistant",
    "content": "Hi there! It’s great to hear from you again! How’s your day going so far? Do you want to jump right into something, or would you like to recap a bit before we start?"
  },
  {
    "role": "user",
    "content": "Lets recap... what is my name?"
  },
  {
    "role": "assistant",
    "content": "Okay, let’s recap! Your name is Fábio. 😊 \n\nAnd just to confirm, today is January 9th, 2025, and it’s 10:20 AM. \n\nWhat’s next?"
  },
  {
    "role": "user",
    "content": "Great! Congrats, Gemma, you are remembering previous conversation sessions!"
  },
  {
    "role": "assistant",
    "content": "That’s fantastic news, Fábio! I’m so glad to hear that I’m remembering our previous sessions correctly. It’s really exciting to see this working! 😊 \n\nNow, what do you want to do?"
  },
  {
    "role": "user",
    "content": "Okay! Tell me what was my first question?"
  },
  {
    "role": "assistant",
    "content": "Okay, let’s see… Your very first question was: “I’m doing quick tests with the chat. Can you help me?”\n\nIs that right? 😊"
  },
  {
    "role": "user",
    "content": "Yes! Perfect!"
  },
  {
    "role": "assistant",
    "content": "Wonderful! I’m so glad we’re on the same page. It’s really rewarding to be able to recall our previous interactions. \n\nSo, what’s our next test or question?"
  },
  {
    "role": "user",
    "content": "I'm going to write a progress report on this... then I'll come back with more tests!"
  },
  {
    "role": "assistant",
    "content": "That sounds like a great plan, Fábio! I’m happy to hear you’re documenting your progress. I’ll be here when you’re ready to run more tests. Good luck with your report! 😊 Let me know if you want to chat while you’re working on it."
  },
  {
    "role": "user",
    "content": "Bye!"
  },
  {
    "role": "assistant",
    "content": "Goodbye, Fábio! I’ll be here when you’re ready to continue. Have a productive day! 😊"
  }
]
```
(prettified with https://jsonformatter.org/)

### Test

I tested the script by beginning with `history.bk` content, exchanged some messages and finished. This created a new `history.json`. If you want to repeat it all, overwrite `history.json` with `history.bk`, ask the same questions, if you get the same answers you will end up with the same `history.json` .
  

## Comments

Gemma3 LLM is quite funny. It is built to divert the user if it does not *know* the answer. When I was testing the script, I accidentally erased the history file, started the script and asked a question. The LLM did not answer that *it doesn't know*, it tried to divert. It makes me think: How is a person aware that he/she does not know? or... that he/she does not know enough (to give a good answer)? In some contexts, *be aware of not knowing* may be a challenge...

