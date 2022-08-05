import os
import torch
 
import time
 
from fastapi import FastAPI



from transformers import AutoTokenizer
from optimum.onnxruntime import ORTModelForCausalLM
import torch

tokenizer = AutoTokenizer.from_pretrained("./onnx3")
model = ORTModelForCausalLM.from_pretrained("./onnx3")

inputs = tokenizer("My name is Philipp and I live in Germany.", return_tensors="pt")

gen_tokens = model.generate(**inputs,do_sample=True,temperature=0.9, min_length=20,max_length=20)
tokenizer.batch_decode(gen_tokens)