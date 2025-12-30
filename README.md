# Notes on LLM Use

## Introduction

Hi, there!

These are my (structured) notes on LLM use. I make notes about anything I regard usefull - they are very scratchy and scattered among devices and applications (PIMs). Sometimes some structure over the notes show up. I write them down and call them *structured notes*.

## How to install and run a LLM locally

I chose to test LLMs running them on a desktop I already have. No specific investment for LLM use, by now. The desktop has core i7-12700 processor with 8GB DDR4-3200 RAM running Ubuntu 22.04 . The tool to test LLMs I chose is Ollama (https://ollama.com/). Just run `curl -fsSL https://ollama.com/install.sh | sh` to install Ollama, as instructed in Ollama site.

To run a model, I followed the instructions in https://docs.ollama.com/quickstart#cli : `ollama run gemma3` this command downloaded, installed and run LLM `gemma` version 3.

At runtime, a prompt was presented and I started chatting with the LLM which I called Gemma. I asked about what data is sent to Google. The answer was that some data can be used by Google and its use is regulated by some agreement. It was clear to me that the context of the answer was that the program was running on Google Cloud... it is curious that the program does not *know* that it is running on a desktop. It also is not programmed to get localhost MAC address.

I fed it with https://www.estadao.com.br/esportes/velocidade/acidente-de-schumacher-completa-12-anos-o-que-se-sabe-sobre-a-saude-do-ex-piloto-de-f1/ brazilian newspaper article and asked some questions about it (with my broken English). The answers included parts of the article translated to English.

 Chat speed was quite good, English translation was very good.
 
 I will try it with the C language standard documentation...
 
 ## 
