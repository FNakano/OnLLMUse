# Notes on LLM Use

## Introduction

Hi, there!

These are my (structured) notes on LLM use. I make notes about anything I regard usefull - they are very scratchy and scattered among devices and applications (PIMs). Sometimes some structure over the notes show up. I write them down and call them *structured notes*.

## How to install and run a LLM locally

I chose to test LLMs running them on a desktop I already have. No specific investment for LLM use, by now. The desktop has core i7-12700 processor with 8GB DDR4-3200 RAM running Ubuntu 22.04 . The tool to test LLMs I chose is Ollama (https://ollama.com/). Just run `curl -fsSL https://ollama.com/install.sh | sh` to install Ollama, as instructed in Ollama site. The command installed Ollama version 0.13.5 .

To run a model, I followed the instructions in https://docs.ollama.com/quickstart#cli : `ollama run gemma3` this command downloaded, installed and run LLM `gemma` version 3.

In runtime, a prompt was presented and I started chatting with the LLM which I called Gemma. I asked about what data is sent to Google. The answer was that some data can be used by Google and its use is regulated by some agreement. It was clear to me that the context of the answer was that the program was running on Google Cloud... it is curious that the program does not *know* that it is running on a desktop. It also is not programmed to get localhost MAC address.

I fed it with https://www.estadao.com.br/esportes/velocidade/acidente-de-schumacher-completa-12-anos-o-que-se-sabe-sobre-a-saude-do-ex-piloto-de-f1/ brazilian newspaper article and asked some questions about it (with my broken English). The answers included parts of the article translated to English.

 Chat speed was quite good, English translation was very good.
 
 I will try it with the C language standard documentation...
 
 ## A shell command to feed LLM with a text file and ask one question
 
 ```
# Assuming you have a file named 'report.txt'
cat report.txt | ollama run gemma3 "Based on the text above, what is the main conclusion?"

```

Tested with `n3220.md`. I converted `n3220.pdf` to markdown using the site https://pdf.ai/tools/pdf-to-markdown . `n3220.pdf` (https://www.open-std.org/jtc1/sc22/wg14/www/docs/n3220.pdf) is, on 2026-01-09, the latest draft of ISO C language standard. Test results are listed below.

<pre><font color="#8AE234"><b>fabio@super</b></font>:<font color="#729FCF"><b>~/Downloads</b></font>$ cat n3220.md | ollama run gemma3 &quot;Based on the text above, how can I use fprintf?&quot;
Based on the provided index, here’s how you can use `fprintf` according to 
the information given:

`fprintf` is a function related to formatted input/output, particularly 
used with wide character input/output functions. Here’s a breakdown of 
relevant details:

*   **Part of Wide Character Input/Output:** It’s linked to “wide 
character input/output function” (322) and “wide character output 
function” (322).
*   **Associated Modifiers:** It’s used with the “wfNformat modifier” 
(332, 340, 418, 423) to handle wide characters.
*   **Functionality:**  It’s a function that allows formatted output to a 
stream, likely used when dealing with wide character data (e.g., Unicode).
*   **Related Functions:** It’s often used in conjunction with functions 
like `wprintf`.
*   **Usage Context:** It’s part of a broader set of functions dealing 
with character conversion and manipulation, particularly when working with 
wide character strings.

**In essence:** `fprintf` is a function that allows you to write formatted 
data (likely Unicode/wide characters) to a stream, leveraging modifiers to 
control the formatting process.
</pre>

Another test:
  
<pre><font color="#8AE234"><b>fabio@super</b></font>:<font color="#729FCF"><b>~/Downloads</b></font>$ cat n3220.md | ollama run gemma3 &quot;Based on the text above, how can I write text on the screen?&quot;
Based on the provided text, you can write text on the screen using the 
following functions:

*   **`wprintf`**: This is a wide-character version of the standard 
`printf` function. It’s used for formatted output of wide characters (wide 
strings).
*   **`wcprintf`**: This is the wide-character version of the `wprintf` 
function.

These functions are part of the wide-character input/output functions, 
which handle wide strings (strings containing characters beyond the ASCII 
range).

</pre>

*comment*: Why it did not mention other functions like `puts`, `printf`?

*Conclusion*: Well,... it returns a useful answer...

## Beyond...

After learning about `ollama` (if you could see the scratchy messy notes...) I can provide some additional information. Installed Ollama version is 0.13.5 and installed `gemma3` model is 4.3B:
  
<pre><font color="#8AE234"><b>fabio@super</b></font>:<font color="#729FCF"><b>~/Downloads</b></font>$ ollama --version
ollama version is 0.13.5
<font color="#8AE234"><b>fabio@super</b></font>:<font color="#729FCF"><b>~/Downloads</b></font>$ ollama list
NAME                    ID              SIZE      MODIFIED     
qwen3:latest            500a1f067a9f    5.2 GB    20 hours ago    
gemma3-tool:latest      3abafa89ad7d    806 MB    28 hours ago    
functiongemma:latest    7c19b650567a    300 MB    46 hours ago    
gemma3:latest           a2af6cc3eb7f    3.3 GB    47 hours ago    
<font color="#8AE234"><b>fabio@super</b></font>:<font color="#729FCF"><b>~/Downloads</b></font>$ ollama show gemma3:latest
  Model
    architecture        gemma3    
    parameters          4.3B      
    context length      131072    
    embedding length    2560      
    quantization        Q4_K_M    

  Capabilities
    completion    
    vision        

  Parameters
    stop           &quot;&lt;end_of_turn&gt;&quot;    
    temperature    1                  
    top_k          64                 
    top_p          0.95               

  License
    Gemma Terms of Use                  
    Last modified: February 21, 2024    
    ...                                 

</pre>

I have two targets:
- How can I get a LLM to remember previous sessions?
  - solved. Reported in https://github.com/FNakano/OnLLMUse/tree/main/history
- How can I get a LLM to run OS or programming language commands?
  - solved. Reported in https://github.com/FNakano/OnLLMUse/tree/main/tool
  
## Index of structured notes

