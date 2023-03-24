Alpaca is a large language model fine-tuned from the [[LLaMA]] 7B model on 52K instruction-following demonstrations, designed to emulate ChatGPT style instruction tuning.  It was created by researchers at Stanford.

The 52K instruction were generated using 175 instruction prompts entered into text-davinci-003, costing $600 in OpenAI API fees and $100 in compute for supervised training.  The initial announcement did not release their model weights as they were waiting on Meta to advise them on when and how they should do it, as at the the time the original LLaMA models were only available through leaked torrents.

They did release their training set and process so the model was recreated by other developers.  [alpaca.cpp](https://github.com/antimatter15/alpaca.cpp), a recreation of the Stanford Alpaca model, was created using LoRA instruct tuning and built on top of llama.cpp.  This was then supported within [Dalai]()

## Links

- [Stanford Alpaca announcment](https://crfm.stanford.edu/2023/03/13/alpaca.html)
- Simon Willison's [Stanford Alpaca, and the acceleration of on-device large language model development](https://simonwillison.net/2023/Mar/13/alpaca/)