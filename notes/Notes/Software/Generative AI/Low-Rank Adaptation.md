Low-Rank Adaptation (LoRA) is a method that is designedto allow full fine-tuning of existing LLMs without having to (expensively) retrain all the model parameters. It works by freezing the model weights of the initial LLM and injecting trainable rank decomcomposition matrices (*I do not understand this*) onto each layer of the Transformer architechture. This reduces the number of parameters used in downstream tasks greatly.  This can reduce the memory requirements significantly, and allows "on-par or better" quality than fine-tuning models.

##  Injecting trainable rank recomposition matrices?

>LoRA finds a subset of the original weights (about 1%) which can be trained to achieve about the same result as training the whole model while using 100x less compute.
>
>Original weights frozen = Rather than modify the original model, the training results are saved to a small file of only a few MB.
>
>In practice this means you can fine tune a 30B parameter model on a consumer GPU in a couple of hours. Without LoRA you would need to run multiple expensive data center GPUs for days or weeks.

[<cite>MacsHeadroom</cite>](https://news.ycombinator.com/item?id=35289168)

> To be more exact, LoRA adds two matrices `A` and `B` to any layers that contain trainable weights. The original weights (`W_0`) have the shape `d × k`. These are frozen. Matrix `A` has dimensions `d × <rank>` (`rank` is configurable) and matrix `B` has the shape `<rank> × k`. A and B are then multiplied and added to `W_0` to get altered weights. The benefit here is that the extra matrices are small compared to `W_0`, which means less parameters need to be optimized, so less activations need to be stored in memory.

[<cite>stephanheijl</cite>](https://news.ycombinator.com/item?id=35289319)

## Wait what is rank

[[Rank]] is the maximal number of linearly independent columns in a matrix.  It has been found that neural networks have low intrinsic rank.

>A neural network contains many dense layers which perform matrix multiplication. The weight matrices in these layers typically have full-rank. When adapting to a specific task, Aghajanyan et al. (2020) shows that the pre-trained language models have a low “instrisic dimension” and can still  learn efficiently despite a random projection to a smaller subspace. Inspired by this, we hypothesize the updates to the weights also have a low “intrinsic rank” during adaptation.

<cite>Hu et al., [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)</cite>

## Wait what is intrensic rank



## Links

- [Original LoRa paper by Microsoft](https://arxiv.org/abs/2106.09685)