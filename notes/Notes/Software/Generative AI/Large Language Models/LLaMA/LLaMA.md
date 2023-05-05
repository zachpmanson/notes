LLaMA is "a collection of foundation language models ranging from 7B to 65B parameters" created by Meta Research. 

> We introduce LLaMA, a collection of foundation language models ranging from 7B to 65B parameters. We train our models on trillions of tokens, and show that it is possible to train state-of-the-art models using publicly available datasets exclusively, without resorting to proprietary and inaccessible datasets. In particular, LLaMA-13B outperforms GPT-3 (175B) on most benchmarks, and LLaMA-65B is competitive with the best models, Chinchilla-70B and PaLM-540B. We release all our models to the research community.

-- [LLaMA: Open and Efficient Foundation Language Models (Abstract)](https://research.facebook.com/publications/llama-open-and-efficient-foundation-language-models/)

It was [announced](https://ai.facebook.com/blog/large-language-model-llama-meta-ai/) and [published](https://research.facebook.com/publications/llama-open-and-efficient-foundation-language-models/) on 2023-02-24 and distributed to selected researchers not long after that.  There were several variants of the model with 7B, 13B, 33B, and 65B parameters.

> In a totally cyberpunk move, within a few days of the release, someone [submitted this PR](https://github.com/facebookresearch/llama/pull/73) to the LLaMA repository linking to an unofficial BitTorrent download link for the model files!

-- [Simon Willison](https://simonwillison.net/2023/Mar/11/llama/)

Simon Willison has interesting writeups on LLaMA and early responses to it:

- [Large language models are having their Stable Diffusion moment](https://simonwillison.net/2023/Mar/11/llama/)
	- discusses the release of LLaMA and llama.cpp
- [Stanford Alpaca, and the acceleration of on-device large language model development](https://simonwillison.net/2023/Mar/13/alpaca/)
	- discusses Dalai and Stanford [[Alpaca]]
- [Could you train a ChatGPT-beating model for $85,000 and run it in a browser?](https://simonwillison.net/2023/Mar/17/beat-chatgpt-in-a-browser/)
	- discusses alpaca.cpp, [[ReAct Prompting]] and the ability to easily expand the capabilities of LLMs, even basic ones
- [llama tag](https://simonwillison.net/tags/llama/) on Willison's blog

## Impact

>Paradoxically, the one clear winner in all of this is Meta. Because the leaked model was theirs, they have effectively garnered an entire planet's worth of free labor. Since most open source innovation is happening on top of their architecture, there is nothing stopping them from directly incorporating it into their products.

-- [Leaked Internal Google Document](https://www.semianalysis.com/p/google-we-have-no-moat-and-neither) on open source LLM progress

## Links

- [llama.cpp](https://github.com/ggerganov/llama.cpp), a port of Facebook's LLaMA model in C/C++
	- designed to run the model using 4-bit [[quantization]] on a MacBook

## Magnets

- [Original LLaMA model weights](magnet:?xt=urn:btih:ZXXDAUWYLRUXXBHUYEMS6Q5CE5WA3LVA&dn=LLaMA)