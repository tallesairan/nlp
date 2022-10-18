
from asyncio import threads
import os
import torch
import time
import json
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from fastapi import Body, FastAPI,Request
from parallelformers import parallelize
from typing import Any, Dict, AnyStr, List, Union
import ast
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
start_time = time.time()

def extractArgumentsFromJson(jsonString):
    jsonData = jsonString["params"]
    return jsonData

def GenerateTextByPayload(payload):
    payloadArguments = extractArgumentsFromJson(payload)
    output  = openai.Completion.create(**payloadArguments)
    end_time = time.time()
    result = {'inference_time': end_time - start_time,
              'result': output
              }
    return result

def TestGenerateTextByPayload(payload):
        
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
        max_new_tokens=payload.tokens, no_repeat_ngram_size=2,num_return_sequences=3,num_beams=5    
    """
    jsonBody = await request.json();
    return GenerateTextByPayload(jsonBody)