#!/usr/bin/env python3
# Copyright (c) 2022 Lincoln D. Stein (https://github.com/lstein)

import os
import time
from fastapi import Body, FastAPI,Request
from typing import Any, Dict, AnyStr, List, Union
# sys.path.append('.')    # corrects a weird problem on Macs?
from ldm.generate import Generate
 
 
 
def extractArgumentsFromJson(jsonString):
    jsonData = jsonString["data"]
    print(type(jsonData))
    return jsonData
 

def GenerateImageByJsonPayload(payload):
    
    start_time = time.time()

 
 
    
    """generate text with hyperparameters
        "prompt": "The quick brown fox jumps over the lazy dog.",
        "num_inference_steps": 50,
        "scale": "7.5",
        "samples": 4,
    
    Returns:
        _type_: array
    """
    
    payloadArguments = extractArgumentsFromJson(payload)
    output = g.txt2img(**payloadArguments)

    end_time = time.time()

    full_output = output
    # output = output['sample'][0]
    result = {'inference_time': end_time - start_time,
            #   'result': output,
              'full_output': full_output
              }
    return result

def TestGenerateImageByJsonPayload(payload):
        
    payloadArguments = extractArgumentsFromJson(payload)
    return payloadArguments
 

def load_generate_instance():
    g = Generate()
    return g

global g
g = load_generate_instance()
g.load_model();

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
    return GenerateImageByJsonPayload(jsonBody)