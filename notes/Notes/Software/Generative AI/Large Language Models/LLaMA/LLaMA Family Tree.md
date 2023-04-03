LLaMA's consequential projects.

- [llama.cpp](https://github.com/ggerganov/llama.cpp) by Georgi Gerganov, a port of Facebook's [[LLaMA]] model in C/C++
	- [bloomz.cpp](https://github.com/NouamaneTazi/bloomz.cpp), a port of BLOOM built on top of llama.cpp
	- [gpt4all](https://github.com/nomic-ai/gpt4all), an assistant-style large language model with ~800k GPT-3.5-Turbo Generations based on LLaMa
- [Dalai](https://github.com/cocktailpeanut/dalai) by @cocktailpeanut, a single command installer to run LLaMa locally with a web interface and API
	- later expanded to include alpaca.cpp
- [Stanford Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html), a model fine-tuned from the LLaMA 7B model on 52K instruction-following demonstrations to function like [[ChatGPT]]
    - [alpaca-lora](https://github.com/tloen/alpaca-lora), a recreation of Stanford [[Alpaca]], based on LLaMA 7B and the Stanford instruction training set using [[Low-Rank Adaptation]] instruct tuning
        - [alpaca.cpp](https://github.com/antimatter15/alpaca.cpp), a fork of llama.cpp that uses alpaca-lora
        - many children of this who have followed the method for the larger LLaMA models, such as [chansung/alpaca-lora-13B](https://huggingface.co/chansung/alpaca-lora-13b) and [chansung/alpaca-lora-30B](https://huggingface.co/chansung/alpaca-lora-30b)
    - [alpaca-native](https://huggingface.co/chavinlo/alpaca-native), a recreation of Standford Alpaca, based on LLaMA 7B and the Stanford instruction training set using native fine-tuning (not LoRA) 
        - [alpaca-native-4bit](https://huggingface.co/ozcur/alpaca-native-4bit), a 4-bit quantisation of alpaca-native made with [GPTQ-for-LLaMA](https://github.com/qwopqwop200/GPTQ-for-LLaMa) (which uses [GPTQ](https://arxiv.org/abs/2210.17323))
    - [Databricks Dolly](https://github.com/databrickslabs/dolly), a model fine-tuned from GPT-J using the Alpaca training set, demonstrating surprisingly high quality instruction following behavior not characteristic of GPT-J
- [Vicuna-13B](https://vicuna.lmsys.org/), a model fine-tuned from LLaMA-13B based on 70k conversations from [ShareGPT](https://sharegpt.com/), with a training method improving upon Alpaca's
