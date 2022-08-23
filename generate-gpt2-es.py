
from asyncio import threads
import os
import torch
import time
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from fastapi import FastAPI

 
def load_models():
    # build model and tokenizer
    model_name_dict = {
		  #'nllb-distilled-600M': 'facebook/nllb-200-distilled-600M',
                  #'nllb-1.3B': 'facebook/nllb-200-1.3B',
                  #'nllb-distilled-1.3B': 'facebook/nllb-200-distilled-1.3B',
                  'distilgpt2': 'DeepESP/gpt2-spanish'
                  #'nllb-3.3B': 'facebook/nllb-200-3.3B',
                  }

    model_dict = {}

    for call_name, real_name in model_name_dict.items():
        print('\tLoading model: %s' % call_name)
        
        ## if you have gpu 
        ##model = AutoModelForCausalLM.from_pretrained(real_name,device=0)
        model = AutoModelForCausalLM.from_pretrained(real_name)
        
        tokenizer = AutoTokenizer.from_pretrained(real_name)
        model_dict[call_name+'_model'] = model
        model_dict[call_name+'_tokenizer'] = tokenizer

    return model_dict


def GenerateText(text,tokens):
    
 
    if len(model_dict) == 2:
        model_name = 'distilgpt2'

    start_time = time.time()
   

    model = model_dict[model_name + '_model']
    tokenizer = model_dict[model_name + '_tokenizer']
        
    generator = pipeline('text-generation',  model=model, tokenizer=tokenizer)
        
    output = generator(text, do_sample=True, temperature=0.9, max_new_tokens=tokens)

    end_time = time.time()

    full_output = output
    output = output[0]['generated_text']
    result = {'inference_time': end_time - start_time,
              'result': output,
              'full_output': full_output
              }
    return result



global model_dict
model_dict = load_models()

app = FastAPI()



@app.get("/")
async def root():
    return {"message": "run /generate?text=&tokens=2048"}

@app.get("/generate")
async def generate(tokens: int = 250, text: str = 'Control Max'):
 
    return {
        "text": text,
        "GenerateText": GenerateText(text,tokens)}

 
