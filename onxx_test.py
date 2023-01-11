from optimum.onnxruntime import ORTQuantizer, ORTModelForCausalLM
from optimum.onnxruntime.configuration import AutoQuantizationConfig
from transformers import AutoTokenizer
from optimum.pipelines import pipeline

model_id = "bertin-project/bertin-gpt-j-6B"
print("Loading model from HuggingFace")
tokenizer = AutoTokenizer.from_pretrained(model_id)

model = ORTModelForCausalLM.from_pretrained(model_id, from_transformers=True, provider="CUDAExecutionProvider")
print("Model loaded")

pipe = pipeline(task="text-generation", model=model, tokenizer=tokenizer,accelerator="ort", device="cuda:0")
result = pipe("Generar una lista de 30 frases distintas sobre el amor:")
print(result)



"""
onnx_gen = pipeline("text-generation", model=model, tokenizer=tokenizer)


text = "Generar una lista de 30 frases distintas sobre el amor:"
gen = onnx_gen(text, max_new_tokens= 1000, use_cache= False, do_sample=True, temperature= 0.1, top_p=0.9, length_penalty=1, top_k=5, no_repeat_ngram_size=2, early_stopping=True)

print(gen)

"""
