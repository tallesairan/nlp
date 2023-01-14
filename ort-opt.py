from transformers import AutoTokenizer
from optimum.onnxruntime import (
  AutoOptimizationConfig,
  ORTModelForCausalLM,
  ORTOptimizer
)
from optimum.onnxruntime.configuration import OptimizationConfig
from optimum.pipelines import pipeline
import sys
import datetime
import time


time_begin = datetime.datetime.fromtimestamp(time.time())

# Load the tokenizer and export the model to the ONNX format
model_id = "bertin-project/bertin-gpt-j-6B"
save_dir = "ort_optimized_model/gptj"

print("Loading Tokenizer : "+model_id+" from huggingface")
tokenizer = AutoTokenizer.from_pretrained(model_id)

print("Loading Model: "+model_id+" from huggingface")
model = ORTModelForCausalLM.from_pretrained(model_id, from_transformers=True)
time_end = datetime.datetime.fromtimestamp(time.time())
print("Time elapsed: ", str(time_end - time_begin))

# Load the optimization configuration detailing the optimization we wish to apply
optimization_config = AutoOptimizationConfig.O3()
print("Optimizing model from pretrained")
optimizer = ORTOptimizer.from_pretrained(model)
time_end = datetime.datetime.fromtimestamp(time.time())
print("Time elapsed: ", str(time_end - time_begin))
print("Saving optimized model to disk")
optimizer.optimize(save_dir=save_dir, optimization_config=optimization_config)
time_end = datetime.datetime.fromtimestamp(time.time())
print("Time elapsed: ", str(time_end - time_begin))
print("Loading ORT optimized model from disk")
model = ORTModelForCausalLM.from_pretrained(save_dir)
time_end = datetime.datetime.fromtimestamp(time.time())
print("Time elapsed: ", str(time_end - time_begin))
onnx_clx = pipeline("text-generation", model=model, accelerator="ort")
text = "Generar una historia de perros mágicos"
pred = onnx_clx(text)
time_end = datetime.datetime.fromtimestamp(time.time())
print("Time elapsed: ", str(time_end - time_begin))
print(pred)

tokenizer.save_pretrained("gptj_ort_optimized")
model.save_pretrained("gptj_ort_optimized")
model.push_to_hub("gptj_ort_optimized", repository_id="gptj_ort_optimized", use_auth_token=True)