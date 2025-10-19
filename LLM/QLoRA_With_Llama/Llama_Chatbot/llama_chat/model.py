
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

def create_quantized_llama():
    model_name = "meta-llama/Llama-3.2-1B-Instruct"

    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype="bfloat16"
    )
    
    quantized_model = AutoModelForCausalLM.from_pretrained(
        model_name,
        quantization_config=bnb_config,
        device_map="auto"
    )
    
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    return quantized_model, tokenizer
