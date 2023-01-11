from transformers import AutoTokenizer, pipeline
from optimum.onnxruntime import ORTModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("bertin-project/bertin-gpt-j-6B")
model = ORTModelForCausalLM.from_pretrained("bertin-project/bertin-gpt-j-6B")
onnx_gen = pipeline("text-generation", model=model, tokenizer=tokenizer)


text = "Generar una lista de 30 frases distintas sobre el amor:"
gen = onnx_gen(text,max_new_tokens=1000,top_k=5,do_sample=True,temperature=0.1,top_p=0.9,early_stopping=True,no_repeat_ngran_size=3)
print(gen)