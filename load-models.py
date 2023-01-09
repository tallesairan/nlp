
from asyncio import threads
import os
import torch
import time
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from fastapi import FastAPI

 
def load_models():
    # build model and tokenizer
    model_name_dict = {
                    'bloom-mt': 'bigscience/bloomz-7b1-mt',
            	    'bloom': 'bigscience/bloom',
                    'gpt-j-6B': 'EleutherAI/gpt-j-6B',
                    'bloom-es': 'jorgeortizfuentes/bloom-1b1-spanish'
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
    return model_dict

 

global model_dict
model_dict = load_models()
