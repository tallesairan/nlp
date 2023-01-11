from optimum.onnxruntime import ORTModelForCausalLM
from optimum.onnxruntime.configuration import AutoQuantizationConfig
from optimum.onnxruntime import ORTQuantizer 
from transformers import pipeline, AutoTokenizer

model_checkpoint = "bertin-project/bertin-gpt-j-6B"
save_directory = "models/onnx/gptj"
# Load a model from transformers and export it to ONNX
print("Loading model from HuggingFace")
ort_model = ORTModelForCausalLM.from_pretrained(model_checkpoint, from_transformers=True)
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
# Save the onnx model and tokenizer
print("Saving model to disk")
ort_model.save_pretrained(save_directory)
tokenizer.save_pretrained(save_directory)
 

# Define the quantization methodology
print("Quantizing model")
qconfig = AutoQuantizationConfig.arm64(is_static=False, per_channel=False)
quantizer = ORTQuantizer.from_pretrained(ort_model)
# Apply dynamic quantization on the model
print("Saving quantized model to disk")
quantizer.quantize(save_dir=save_directory, quantization_config=qconfig)
# Load the quantized model
print("Loading quantized model from disk")
model = ORTModelForCausalLM.from_pretrained(save_directory, file_name="model_quantized.onnx")
tokenizer = AutoTokenizer.from_pretrained(save_directory)
## Generate text using the quantized model
print("Generating text using the quantized model")
cls_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)
results = cls_pipeline("Generar una lista de 30 frases distintas sobre el amor:")
print(results)
"""
tokenizer = AutoTokenizer.from_pretrained("bertin-project/bertin-gpt-j-6B")
model = ORTModelForCausalLM.from_pretrained("./onnx/",local_files_only=True)
onnx_gen = pipeline("text-generation", model=model, tokenizer=tokenizer)


text = "Generar una lista de 30 frases distintas sobre el amor:"
gen = onnx_gen(text,max_new_tokens=500,top_k=5,do_sample=True,temperature=0.1,top_p=0.9,early_stopping=True,no_repeat_ngran_size=3)
print(gen)
"""