import sys
import os
import time
from transformers import AutoTokenizer, AutoModelForCausalLM, GPTJForCausalLM, pipeline


model = sys.argv[1:]
model_name = model[0]

save_path = os.path.join(os.getcwd(), 'export-models/' + model_name)

print("Loading " + model_name + " model from HuggingFace")

model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

print("Model loaded")
print("Saving model  " + model_name + " to "+save_path)
model.save_pretrained(save_path)
tokenizer.save_pretrained(save_path)



