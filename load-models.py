
from asyncio import threads
import os
import torch
import time
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from fastapi import FastAPI
import transformers.onnx as onnx

import subprocess
def load_models():
    # build model and tokenizer
    model_name_dict = {
                  'gpt-j': 'bertin-project/bertin-gpt-j-6B'
            	    #'bloom': 'bigscience/bloom',
                    #'gpt-j-6B': 'EleutherAI/gpt-j-6B',
                    #'bloom-es': 'jorgeortizfuentes/bloom-1b1-spanish'
                    # 'distilgpt2': 'distilgpt2',
                    # 'nllb-distilled': 'facebook/nllb-200-distilled-1.3B',
                    # 'opus-mt-mul-en': 'Helsinki-NLP/opus-mt-mul-en',
                    # 'bertin-gpt-j-6B':'bertin-project/bertin-gpt-j-6B'
                }

    model_dict = {}


    for call_name, real_name in model_name_dict.items():
        print('\tLoading model: %s' % call_name)
        
        ## GPTJ WITH CUDA
        #model = AutoModelForCausalLM.from_pretrained(real_name,  device=0, low_cpu_mem_usage=True) 
        # GPTJ CPU ONLY
        model = AutoModelForCausalLM.from_pretrained(real_name)
        tokenizer = AutoTokenizer.from_pretrained(real_name)
        model_dict[call_name+'_model'] = model
        model_dict[call_name+'_tokenizer'] = tokenizer
        print('\tLoaded model: %s' % call_name)
        print('\tSaving model: %s' % call_name)
        model_dict[call_name+'_model'].save_pretrained('models/'+call_name)
        print('\tSaved model, saving tokenizer: %s' % call_name)
        model_dict[call_name+'_tokenizer'].save_pretrained('models/'+call_name)

        p = subprocess.Popen("python -m transformers.onnx --model="+'models/'+call_name+" --feature=causal-lm onnx/", stdout=subprocess.PIPE, shell=True)

        print(p.communicate())

    return model_dict

 

global model_dict
model_dict = load_models()
