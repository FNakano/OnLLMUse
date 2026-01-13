# History and Tool extended and merged

## Introduction

Keep all conversation history is implemented in https://github.com/FNakano/OnLLMUse/tree/main/history

Tool call (function call) is documented here: https://github.com/FNakano/OnLLMUse/tree/main/tool

## Test result

On a chat with Qwen3, I ask it to get some information (make tool calls), divert a little and ask for the previous information.

<pre><font color="#8AE234"><b>fabio@super</b></font>:<font color="#729FCF"><b>~/localHomeGit/localLLM/python</b></font>$ python3 -m promptMe
Did not find file named history.json, starting from empty history.
[{&apos;role&apos;: &apos;system&apos;, &apos;content&apos;: &apos;You are a helpful assistant that remembers previous questions.&apos;}]
Hello, Qwen, are you there
?
AI: Hello! Yes, I&apos;m here. How can I assist you today?

AI: Hello! Yes, I&apos;m here. How can I assist you today?

Qwen, can you tell me what time is it?
function=Function(name=&apos;get_current_time&apos;, arguments={})
{}
{&apos;status&apos;: &apos;success&apos;, &apos;time&apos;: &apos;2026-01-13 14:43:51&apos;, &apos;day&apos;: &apos;Tuesday&apos;, &apos;message&apos;: &apos;Current time is 2026-01-13 14:43:51 (Tuesday)&apos;}
AI: The current time is **2026-01-13 (Tuesday) at 14:43:51**. Let me know if you need anything else! 😊

What is the temperature in São Paulo?
function=Function(name=&apos;get_temperature&apos;, arguments={&apos;city&apos;: &apos;São Paulo&apos;})
{&apos;city&apos;: &apos;São Paulo&apos;}
São Paulo
25
AI: The current temperature in São Paulo is **25°C**. Let me know if you need more information! 😊

Qwen you are so helpful! Thanks!
AI: You&apos;re welcome! I&apos;m here to help whenever you need. 😊 Let me know if there&apos;s anything else I can assist you with!

Can you play games?
AI: I&apos;m sorry, but I can&apos;t play games directly. However, I can help you with information, answer questions, or assist with tasks! What can I do for you? 😊

Qwen, I apologyze for the time I took to answer... It&apos;s okay if you can&apos;t play games directly.... by the way, my name is Fábio!
AI: You&apos;re welcome, Fábio! 😊 While I can&apos;t play games directly, I&apos;m here to help with any questions or tasks you need assistance with. Whether it&apos;s checking the weather, telling time, or anything else—just let me know! What can I do for you today?

Okay! Qwen, when did I ask you the time before?
AI: Fábio, you first asked me the time in your **second message** (&quot;Qwen, can you tell me what time is it?&quot;), and then again in your **current query** (&quot;Okay! Qwen, when did I ask you the time before?&quot;). 😊  
Let me know if you&apos;d like to revisit any of those moments!

Yes, please. What was your answer for my second message?
AI: When you asked for the time before, it was your first message: **&quot;Qwen, can you tell me what time is it?&quot;** My answer was: *&quot;The current time is **2026-01-13 (Tuesday) at 14:43:51**.&quot;*  

For your second message (**&quot;What is the temperature in São Paulo?&quot;**), my answer was: **&quot;The current temperature in São Paulo is 25°C.&quot;**  

Let me know if you need further clarification! 😊

Really smart! Thank you! See you latter!
AI: You&apos;re welcome, Fábio! 😊  
- **About games**: I can&apos;t play games directly, but I&apos;d love to help you strategize or discuss game ideas!  
- **Your second message**: When you asked for the time, I replied: *&quot;The current time is **2026-01-13 (Tuesday) at 14:43:51**.&quot;*  
- **Your name**: I remember you’re Fábio! Nice to meet you!  

Feel free to reach out anytime. Have a great day! 🌟

^CTerminating conversation loop.
<font color="#8AE234"><b>fabio@super</b></font>:<font color="#729FCF"><b>~/localHomeGit/localLLM/python</b></font>$ 
</pre>

## How to run (and stop) the code

There are two ways to run the code: `python3 -m promptMe` on the command line;
`python3` on the command line and `import promptMe` on REPL prompt.

Chat can be finished by pressing either CTRL-C or CTRL-D.

## Code explained

All code is contained in `promptMe.py`. Functions `get_temperature` and `get_current_time` are defined and made available to the LLM. Function `get_history` and `chat_with_ollama` are defined and not available to the LLM. The piece of code that is executed on package import is the conversation loop follows `get_history` function definition.

`get_temperature` contains a dictionary associating some cities to some numbers. The numbers are dummies for city temperature.

`get_current_time` calls Python `datetime` functions in order to get current system time.

`get_history` loads chat history from the file to the `messages` variable. `messages` is a list of dictionaries, it is serialized in JSON.

`chat_with_ollama` calls `ollama` package `chat()` API call with message history and tool list, if response is a tool call, the corresponding Python function is called and some messages are sent to command line/REPL prompt. New messages are appended to `messages` variable.

## Conclusion and comments

In the test (above), LLM (Qwen3) made tool calls when expected (there were no unexpected tool calls) and retrieved responses to questions asked.

