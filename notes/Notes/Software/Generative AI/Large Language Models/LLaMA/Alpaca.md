Alpaca is a large language model fine-tuned from the [[LLaMA]] 7B model on 52K instruction-following demonstrations, designed to emulate ChatGPT style instruction tuning.  It was created by researchers at Stanford.

The 52K instruction were generated using 175 instruction prompts entered into text-davinci-003, costing $600 in OpenAI API fees and $100 in compute for supervised training.  The initial announcement did not release their model weights as they were waiting on Meta to advise them on when and how they should do it, as at the the time the original LLaMA models were only available through leaked torrents.

They did release their training set and process so the model was recreated by other developers.  [alpaca.cpp](https://github.com/antimatter15/alpaca.cpp), a recreation of the Stanford Alpaca model, was created using [[Low-Rank Adaptation]] (LoRA) instruct tuning and built on top of llama.cpp.  This was then supported within [Dalai](https://github.com/cocktailpeanut/dalai).

[alpaca-native](https://huggingface.co/chavinlo/alpaca-native) is a recreation of Standford Alpaca, based on LLaMA 7B and the Stanford instruction training set using native fine-tuning (not LoRA).  This methodology was used by others to create similar models based the larger LLaMA models (see [[LLaMA Family Tree]]).

## Links

- [Stanford Alpaca announcment](https://crfm.stanford.edu/2023/03/13/alpaca.html)
- Simon Willison's [Stanford Alpaca, and the acceleration of on-device large language model development](https://simonwillison.net/2023/Mar/13/alpaca/)

## Magnets

- alpaca.cpp 
	- [7B model weights ggml-alpaca-7b-q4.bin](magnet:?xt=urn:btih:5aaceaec63b03e51a98f04fd5c42320b2a033010&dn=ggml-alpaca-7b-q4.bin&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Fopentracker.i2p.rocks%3A6969%2Fannounce), 4.21GB
	- [13B model weights](magnet:?xt=urn:btih:f3cf71b172129d6b5abccab393bc32253fac8159&dn=ggml-alpaca-13b-q4.bin&tr=udp%3A%2F%http://2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%https://t.co/zenhelfwRd%3A6969%2Fannounce&tr=https%3A%2F%https://t.co/zenhelfwRd%3A443%2Fannounce&tr=udp%3A%2F%https://t.co/RRAn1X65wE%3A6969%2Fannounce&tr=udp%3A%2F%https://t.co/uTXBeTLUMa%3A2810%2Fannounce)