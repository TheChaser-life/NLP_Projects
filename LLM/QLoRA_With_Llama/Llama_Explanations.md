# EXPLANATIONS ABOUT LLAMA MODELS
Note: This explanation based on my opinion about Llama so it can be wrong somewhere

<img width="300" height="168" alt="image" src="https://github.com/user-attachments/assets/0f470e58-d5ee-4c1c-90a3-300f31cc5709" />

Llama 3.2 (or another version) is a large language model developed by Meta AI. It ís designed based on transformers decoder structure (decoder-only) just like GPT

<img width="1640" height="862" alt="image" src="https://github.com/user-attachments/assets/fa610b81-c5e2-46ac-a634-6068452f13f7" />

Llama structure:

<img width="934" height="1572" alt="image" src="https://github.com/user-attachments/assets/d89a6295-87ee-4285-8030-ef905d32dab5" />


1. Tokenizer : using BPE/SentencePiece algorithm to tokenize text
2. Embedding layer : mapping the token id into its embedding vector, about the positional embedding, LLama 3.2 uses rotary position embedding (RoPE)
3. Transformers_Decoder blocks (a sequence of transformers_decoder blocks), inside a transformer decoder:
   + Layer Norm : normalize values go through it
   + Self-Attention layer : help model focus on the important part of the input with the querry, key, value vector
   + Residual-Connection layer : avoid vanishing gradient due to long input text
   + Feed-Forward Network : expand input dimesion then apply GELU function (for non-linear representation) and after that turn the input back to the previous dimension
4. Final Layer Norm : normalize values before it go to the output head
5. Output Head : map the input from hidden size to vocab size then apply the softmax to predict the next token 
   

