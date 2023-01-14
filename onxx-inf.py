from optimum.onnxruntime import ORTModelForCausalLM
from optimum.onnxruntime.configuration import AutoQuantizationConfig
from optimum.onnxruntime import ORTQuantizer 
from transformers import pipeline, AutoTokenizer

model_checkpoint = "bertin-project/bertin-gpt-j-6B"
save_directory = "models/onnx/gptj"
save_directory_alt = "models/pretrained/gptj"
# Load a model from transformers and export it to ONNX
print("Loading model from HuggingFace")
ort_model = ORTModelForCausalLM.from_pretrained(model_checkpoint, from_transformers=True)
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
# Save the onnx model and tokenizer




#print("Saving model to disk")
#ort_model.save_pretrained(save_directory_alt)
#tokenizer.save_pretrained(save_directory_alt)
 
"""

 
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