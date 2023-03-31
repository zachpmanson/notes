>Fine-tuning enormous language models is prohibitively expensive in terms of the hardware required and the storage/switching cost for hosting independent instances for different tasks. We propose LoRA, an efficient adaptation strategy that neither introduces inference latency nor reduces input sequence length while retaining high model quality

<cite>Hu et al., [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)</cite>

Low-Rank Adaptation (LoRA) is a method that is designed to allow full fine-tuning of existing LLMs without having to (expensively) retrain all the model parameters, and avoids additional inference latency. It works by freezing the model weights of the initial LLM and injecting trainable rank decomcomposition matrices onto each layer of the Transformer architechture. This reduces the number of parameters used in downstream tasks greatly.  This can reduce the memory requirements significantly, and allows "on-par or better" quality than fine-tuning models.

LoRA was initially explored as a technique for use in LLMs but is also applicable to other kinds of models. [It is used](https://replicate.com/blog/lora-faster-fine-tuning-of-stable-diffusion) to fine-tune [[Stable Diffusion]] models faster than other tools like Dreambooth.

>While we focused on Transformer language models, the proposed principles are generally applicable to any neural networks with dense layers.

<cite>Hu et al., [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)</cite>

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

## Wait what is intrensic dimensionality

> the **intrinsic dimensionality** of a space is the number of _required_ pieces of information that we need to describe each object in the space, which may differ from the number of pieces of information that we _are_ using, which we call the **extrinsic dimensionality** of the space

<cite>Matthew N. Bernstein</cite>, in his [very good writeup](https://mbernste.github.io/posts/intrinsic_dimensionality/)

This in essence means that the dimensionality that is actually needed may be lower than the full dimensionality of the matrix.  A simple example of this is imagining a set of points on a 2D place that exists within a 3D space.  This has 3 extrensic dimensions, but since only 2 are actually needed to describe points, it has 2 intrensic dimensions.

## So what is intrensic rank

I guess intrensic rank is the *required* maximal number of linearly independent columns in a matrix, as opposited to the extrensic rank which is the number of linearly indepedent columns.

>Extrinsic rank is an objective property of a matrix that is based solely on its entries, while intrinsic rank takes into account the structure and patterns of the data, and it can be lower than the extrinsic rank in cases where the data has low-dimensional structure or redundancy.

<cite>ChatGPT</cite>

## Links

- [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685), the original LoRA paper by Microsoft