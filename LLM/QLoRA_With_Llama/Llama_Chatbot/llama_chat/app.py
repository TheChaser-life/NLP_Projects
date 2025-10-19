
import gradio as gr
import os
import torch

from model import create_quantized_llama
from timeit import default_timer as timer
from typing import Tuple, Dict
from peft import PeftModel

model, tokenizer = create_quantized_llama()

peft_model = PeftModel.from_pretrained(model,"adapter.pth")

device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
peft_model.to(device)

def response(text,history):
    start_time = timer()

    messages = [{"role":"system","content":"You are a helpful assistant."}]

    for user, bot in history:
        messages.append({"role":"user","content":user})
        messages.append({"role":"assistant","content":bot})
    messages.append({"role":"user","content":text})
    
    inputs = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        tokenize=True,
        return_dict=True,
        return_tensors="pt"
    ).to(device)
    
    outputs = peft_model.generate(**inputs, max_new_tokens=100)
    running_time = round(timer() - start_time,5)
    return tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True)),running_time
    

title = 'Llama 3.2 chatbot 🤖'
des = 'A model based on Llama 3.2 1B instruct'
article = "Finetuned with alpaca dataset"

examples = [
    "What is the capital of France?",
    "How did Julius Caeser die?",
    "Given two examples of a liquid."
]

demo = gr.ChatInterface(fn=response,
                    examples=examples,
                    title=title,
                    description=des,
                    article=article)
demo.launch()
