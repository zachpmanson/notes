Low-Rank Adaptation (LoRa) is a method that is designedto allow full fine-tuning of existing LLMs without having to (expensively) retrain all the model parameters. It works by freezing the model weights of the initial LLM and injecting trainable rank decomcomposition matrices (*I do not understand this*) onto each layer of the Transformer architechture. This reduces the number of parameters used in downstream tasks greatly.  This can reduce the memory requirements significantly, and allows "on-par or better" quality than fine-tuning models.

## Links

- [Original LoRa paper by Microsoft](https://arxiv.org/abs/2106.09685)