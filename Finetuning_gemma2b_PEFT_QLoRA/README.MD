This notebook has all the steps required to fine-tune the gemma-2b or Llama-2-7b-hf model with 7 billion parameters on a T4 GPU. 
You have the option to use a free GPU on Google Colab or Kaggle. This code can run on both platforms.

The Colab T4 GPU has a limited 16 GB of VRAM. That is barely enough to store Llama 2–7b's weights, 
which means full fine-tuning is not possible, and we need to use parameter-efficient fine-tuning techniques like LoRA or QLoRA.

We will use the QLoRA technique to fine-tune the model in 4-bit precision and optimize VRAM usage. 
For that, we will use the Hugging Face ecosystem of LLM libraries: transformers, accelerate, peft, trl, and bitsandbytes.

Checkout [medium article](https://medium.com/@0192.mayuri/efficient-fine-tuning-of-ai-models-with-lora-and-qlora-69efdb2a3faf) to know concepts in detail.
