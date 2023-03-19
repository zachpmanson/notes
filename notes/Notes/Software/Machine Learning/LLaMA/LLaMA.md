LLaMA is "a collection of foundation language models ranging from 7B to 65B parameters" created by Meta Research. 

> We introduce LLaMA, a collection of foundation language models ranging from 7B to 65B parameters. We train our models on trillions of tokens, and show that it is possible to train state-of-the-art models using publicly available datasets exclusively, without resorting to proprietary and inaccessible datasets. In particular, LLaMA-13B outperforms GPT-3 (175B) on most benchmarks, and LLaMA-65B is competitive with the best models, Chinchilla-70B and PaLM-540B. We release all our models to the research community.

<cite>LLaMA paper abstract</cite>

It was [announced](https://ai.facebook.com/blog/large-language-model-llama-meta-ai/) and [published](https://research.facebook.com/publications/llama-open-and-efficient-foundation-language-models/) on 2023-02-24 and distributed to selected researchers not long after that.  There were several variants of the model with 7B, 13B, 33B, and 65B parameters.

> In a totally cyberpunk move, within a few days of the release, someone [submitted this PR](https://github.com/facebookresearch/llama/pull/73) to the LLaMA repository linking to an unofficial BitTorrent download link for the model files!

[<cite>Simon Willison</cite>](https://simonwillison.net/2023/Mar/11/llama/)

Simon Willison has interesting writeups on LLaMA and early responses to it:

- [Large language models are having their Stable Diffusion moment](https://simonwillison.net/2023/Mar/11/llama/)
	- discusses the release of LLaMA and llama.cpp
- [Stanford Alpaca, and the acceleration of on-device large language model development](https://simonwillison.net/2023/Mar/13/alpaca/)
	- discusses Dalai and Stanford Alpaca
- [Could you train a ChatGPT-beating model for $85,000 and run it in a browser?](https://simonwillison.net/2023/Mar/17/beat-chatgpt-in-a-browser/)
	- discusses alpaca.cpp, [[ReAct prompting]] and the ability to easily expand the capabilities of LLMs, even basic ones
- [llama tag](https://simonwillison.net/tags/llama/) on Willison's blog

## Consequential Projects

- [llama.cpp](https://github.com/ggerganov/llama.cpp) by Georgi Gerganov, a port of Facebook's LLaMA model in C/C++
	- [bloomz.cpp](https://github.com/NouamaneTazi/bloomz.cpp), a port of BLOOM built on top of llama.cpp
- [Dalai](https://github.com/cocktailpeanut/dalai) by @cocktailpeanut, a single command installer to run LLaMa locally with a web interface and API
	- later expanded to include alpaca.cpp
- [Stanford Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html), a model fine-tuned from the LLaMA 7B model on 52K instruction-following demonstrations to function like [[ChatGPT]]
	- [alpaca-lora](https://github.com/tloen/alpaca-lora), a recreation of the Stanford Alpaca model, based on LLaMa 7B and the Stanford instruction training set using [[Low-Rank Adaptation]] instruct tuning
		- [alpaca.cpp](https://github.com/antimatter15/alpaca.cpp), a fork of llama.cpp that uses alpaca-lora


## Magnets

- [Original LLaMA model weights](magnet:?xt=urn:btih:ZXXDAUWYLRUXXBHUYEMS6Q5CE5WA3LVA&dn=LLaMA)
- alpaca.cpp 
	- [7B model weights ggml-alpaca-7b-q4.bin](magnet:?xt=urn:btih:5aaceaec63b03e51a98f04fd5c42320b2a033010&dn=ggml-alpaca-7b-q4.bin&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Fopentracker.i2p.rocks%3A6969%2Fannounce), 4.21GB
	- [13B model weights](magnet:?xt=urn:btih:f3cf71b172129d6b5abccab393bc32253fac8159&dn=ggml-alpaca-13b-q4.bin&tr=udp%3A%2F%http://2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%https://t.co/zenhelfwRd%3A6969%2Fannounce&tr=https%3A%2F%https://t.co/zenhelfwRd%3A443%2Fannounce&tr=udp%3A%2F%https://t.co/RRAn1X65wE%3A6969%2Fannounce&tr=udp%3A%2F%https://t.co/uTXBeTLUMa%3A2810%2Fannounce)