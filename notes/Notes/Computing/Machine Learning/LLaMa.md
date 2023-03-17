LLaMa is "a collection of foundation language models ranging from 7B to 65B parameters" created by Meta Research. 

> We introduce LLaMA, a collection of foundation language models ranging from 7B to 65B parameters. We train our models on trillions of tokens, and show that it is possible to train state-of-the-art models using publicly available datasets exclusively, without resorting to proprietary and inaccessible datasets. In particular, LLaMA-13B outperforms GPT-3 (175B) on most benchmarks, and LLaMA-65B is competitive with the best models, Chinchilla-70B and PaLM-540B. We release all our models to the research community.

<cite>LLaMa paper abstract</cite>

It was [announced](https://ai.facebook.com/blog/large-language-model-llama-meta-ai/) and [published](https://research.facebook.com/publications/llama-open-and-efficient-foundation-language-models/) on 2023-02-24 and distributed to selected researchers not long after that.  There were several variants of the model with 7B, 13B, 33B, and 65B parameters.

> In a totally cyberpunk move, within a few days of the release, someone [submitted this PR](https://github.com/facebookresearch/llama/pull/73) to the LLaMA repository linking to an unofficial BitTorrent download link for the model files!

[<cite>Simon Willison</cite>](https://simonwillison.net/2023/Mar/11/llama/)

Simon Willison has interesting writeups on LLaMa and early responses to it:

- [Large language models are having their Stable Diffusion moment](https://simonwillison.net/2023/Mar/11/llama/)
- [Stanford Alpaca, and the acceleration of on-device large language model development](https://simonwillison.net/2023/Mar/13/alpaca/)
- [llama tag](https://simonwillison.net/tags/llama/) on Willison's blog

## Consequential Projects

- [llama.cpp](https://github.com/ggerganov/llama.cpp) by Georgi Gerganov, a port of Facebook's LLaMA model in C/C++
- [Dalai](https://github.com/cocktailpeanut/dalai) by @cocktailpeanut, a single command installer to run LLaMa locally with a web interface and API
- [Stanford Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html), a model fine-tuned from the LLaMA 7B model on 52K instruction-following demonstrations to function like [[ChatGPT]]
- [alpaca.cpp](https://github.com/antimatter15/alpaca.cpp), a recreation of the Stanford Alpaca model, based on LLaMa 7B and the Stanford instruction training set using LoRA instruct tuning
