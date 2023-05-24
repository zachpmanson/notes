## In General

>Quantization is the process of constraining an input from a continuous or otherwise large set of values (such as the real numbers) to a discrete set (such as the integers)

-- [Wikipedia - Quantization](https://en.wikipedia.org/wiki/Quantization)

## In Machine Learning 

>Quantization is a technique to reduce the computational and memory costs of running inference by representing the weights and activations with low-precision data types like 8-bit integer (`int8`) instead of the usual 32-bit floating point (`float32`).

-- [Hugging Face Optimum Documentation](https://huggingface.co/docs/optimum/concept_guides/quantization)

Depending on the model size and the level of quantization used, quantization can result in significant improvements in performance without major degradation of output quality.