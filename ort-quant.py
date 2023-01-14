from transformers import AutoTokenizer
from optimum.onnxruntime import (
  AutoQuantizationConfig,
  ORTModelForCausalLM,
  ORTQuantizer,
  ORTOptimizer
)
from optimum.pipelines import pipeline
import sys
import datetime
import time


class ClockPS1(object):
    def __repr__(self):
        now = datetime.datetime.now()
        return str(now.strftime("%H:%M:%S >>> "))


sys.ps1 = ClockPS1()
# Load the tokenizer and export the model to the ONNX format

model_id = "bertin-project/bertin-gpt-j-6B"
save_dir = "quantized_model/gptj"
time_begin = datetime.datetime.fromtimestamp(time.time())

print("Loading model from HuggingFace")
model = ORTModelForCausalLM.from_pretrained(model_id, from_transformers=True)
print("Model loaded")
time_end = datetime.datetime.fromtimestamp(time.time())
print("Time elapsed: ", str(time_end - time_begin))
# Load the quantization configuration detailing the quantization we wish to apply
qconfig = AutoQuantizationConfig.avx512_vnni(is_static=False, per_channel=True)
print("Quantizing model")
quantizer = ORTQuantizer.from_pretrained(model)

print("Saving quantized model to disk")
# Apply dynamic quantization and save the resulting model
quantizer.quantize(save_dir=save_dir, quantization_config=qconfig)
time_end = datetime.datetime.fromtimestamp(time.time())
print("Time elapsed: ", str(time_end - time_begin))
print("Loading quantized model from disk")
# Load the quantized model from a local repository
model = ORTModelForCausalLM.from_pretrained(save_dir)
print("Model loaded")
time_end = datetime.datetime.fromtimestamp(time.time())

print("Time elapsed: ", str(time_end - time_begin))
# Create the transformers pipeline
print("Creating pipeline")
onnx_clx = pipeline("text-generation", model=model, accelerator="ort")
print("Pipeline loaded")
text = "Generar una lista de 30 frases sobre amor:"
print("Generating text using the quantized model....")
pred = onnx_clx(text)
print(pred)

print("Time elapsed: ", str(time_end - time_begin))
