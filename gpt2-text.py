
import os
import torch
 
import time

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from flores200_codes import flores_codes
from fastapi import FastAPI

 
def load_models():
    # build model and tokenizer
    model_name_dict = {
		  #'nllb-distilled-600M': 'facebook/nllb-200-distilled-600M',
                  #'nllb-1.3B': 'facebook/nllb-200-1.3B',
                  #'nllb-distilled-1.3B': 'facebook/nllb-200-distilled-1.3B',
                  'gpt-j': 'EleutherAI/gpt-j-6B'
                  #'nllb-3.3B': 'facebook/nllb-200-3.3B',
                  }

    model_dict = {}

    for call_name, real_name in model_name_dict.items():
        print('\tLoading model: %s' % call_name)
        model = AutoModelForCausalLM.from_pretrained(real_name)
        tokenizer = AutoTokenizer.from_pretrained(real_name)
        model_dict[call_name+'_model'] = model
        model_dict[call_name+'_tokenizer'] = tokenizer

    return model_dict


def GenerateText(text):
    
    if not torch.backends.mps.is_available():
        if not torch.backends.mps.is_built():
            print("MPS not available because the current PyTorch install was not "
            "built with MPS enabled.")
        else:
            print("MPS not available because the current MacOS version is not 12.3+ "
                "and/or you do not have an MPS-enabled device on this machine.")
        
    else:
            print("Setting MPS as default device")
            mps_device = torch.device("mps")
        
        
        
    if len(model_dict) == 2:
        model_name = 'gpt-j'

    start_time = time.time()
   

    model = model_dict[model_name + '_model']
    tokenizer = model_dict[model_name + '_tokenizer']
    
    
    if not torch.backends.mps.is_available():
        if not torch.backends.mps.is_built():
            print("MPS not available because the current PyTorch install was not "
                "built with MPS enabled.")
        else:
            print("MPS not available because the current MacOS version is not 12.3+ "
                "and/or you do not have an MPS-enabled device on this machine.")
            


        mps_device = torch.device("mps")
        generator = pipeline('text-generation',  model=model, device=mps_device, tokenizer=tokenizer)


    else:
        print("Using default device")
        generator = pipeline('text-generation',  model=model, tokenizer=tokenizer)

        
            
    output = generator(text,max_new_tokens=1024)

    end_time = time.time()

    full_output = output
    output = output[0]['generated_text']
    result = {'inference_time': end_time - start_time,
              'result': output,
              'full_output': full_output
              }
    return result
    """
    """

global model_dict
model_dict = load_models()

app = FastAPI()



@app.get("/")
async def root():
    return {"message": "run /generate?source=&target=&text="}

@app.get("/generate")
async def generate(text: str = 'loirinha rabuda'):
 
    return {
        "text": text,
        "GenerateText": GenerateText(text)}

 
