
from asyncio import threads
import os
from dotenv import load_dotenv
import torch
import time
import json
from diffusers import StableDiffusionPipeline
from fastapi import Body, FastAPI,Request
from parallelformers import parallelize
from typing import Any, Dict, AnyStr, List, Union
import ast
 
load_dotenv()
AUTH_TOKEN = os.getenv("HF_AUTH_TOKEN")
os.environ["CUDA_VISIBLE_DEVICES"]=""

def load_models():
    # build model and tokenizer //
    model_name_dict = {
        'stable': 'CompVis/stable-diffusion-v1-4'
    }

    model_dict = {}

    for call_name, real_name in model_name_dict.items():
        print('\tLoading model: %s' % call_name)
        
        ## GPTJ WITH CUDA
        #model = AutoModelForCausalLM.from_pretrained(real_name, low_cpu_mem_usage=True) 
        #parallelize(model, num_gpus=2, fp16=True, verbose='detail')
        
        # GPTJ CPU ONLY
        model = StableDiffusionPipeline.from_pretrained(real_name, revision="fp16", torch_dtype=torch.float16, low_cpu_mem_usage=True, use_auth_token=AUTH_TOKEN)
        #model = StableDiffusionPipeline.from_pretrained(real_name, revision="fp16", torch_dtype=torch.float16, use_auth_token=AUTH_TOKEN)
        model_dict[call_name+'_model'] = model

    return model_dict



"""
 
"""
 
 
def extractArgumentsFromJson(jsonString):
    jsonData = jsonString["data"]
    print(type(jsonData))
    return jsonData
 

def GenerateTextByPayload(payload):
    

 

    start_time = time.time()
   

    model = model_dict['stable_model']
        
    # First Test -> Quechua   
    #output = generator(text,  top_p=1, top_k=12, length_penalty=0, do_sample=True, temperature=1.33, max_new_tokens=tokens)
    
    
    """generate text with hyperparameters
        "prompt": "The quick brown fox jumps over the lazy dog.",
        "num_inference_steps": 50,
        "scale": "7.5",
        "samples": 4,
    
    Returns:
        _type_: array
    """
    
    payloadArguments = extractArgumentsFromJson(payload)
    output = model(**payloadArguments)

    end_time = time.time()

    full_output = output
    output = output['sample'][0]
    result = {'inference_time': end_time - start_time,
              'result': output,
              'full_output': full_output
              }
    return result

def TestGenerateTextByPayload(payload):
        
    payloadArguments = extractArgumentsFromJson(payload)
    return payloadArguments

global model_dict
model_dict = load_models()

app = FastAPI()

JSONObject = Dict[AnyStr, Any]
JSONArray = List[Any]
JSONStructure = Union[JSONArray, JSONObject]

@app.get("/")
async def root():
    return {"message": "run /generate?text=&tokens=2048"}

@app.post("/inference")
async def inference(request: Request):
    """
       prompt, num_inference_steps, scale, samples
    """
    jsonBody = await request.json();
    return GenerateTextByPayload(jsonBody)