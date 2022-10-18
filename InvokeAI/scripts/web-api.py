#!/usr/bin/env python3
# Copyright (c) 2022 Lincoln D. Stein (https://github.com/lstein)

import os
import re
import sys
import shlex
import copy
import warnings
import time
import traceback
import torch
import time
import json
from diffusers import StableDiffusionPipeline
from fastapi import Body, FastAPI,Request
from parallelformers import parallelize
from typing import Any, Dict, AnyStr, List, Union
import ast
sys.path.append('.')    # corrects a weird problem on Macs
from ldm.generate import Generate
 
 
 
def extractArgumentsFromJson(jsonString):
    jsonData = jsonString["data"]
    print(type(jsonData))
    return jsonData
 

def GenerateImageByJsonPayload(payload):
    
    start_time = time.time()

    g = Generate()
 
 
    
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