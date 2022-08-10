
from asyncio import threads
import os
import torch
import time
import json
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from fastapi import Body, FastAPI
from parallelformers import parallelize


 
def load_models():
    # build model and tokenizer
    model_name_dict = {
                  'gpt-j': 'EleutherAI/gpt-j-6B'
                  }

    model_dict = {}

    for call_name, real_name in model_name_dict.items():
        print('\tLoading model: %s' % call_name)
        
        ## GPTJ WITH CUDA
        #model = AutoModelForCausalLM.from_pretrained(real_name,  device=0, low_cpu_mem_usage=True) 
        # GPTJ CPU ONLY
        model = AutoModelForCausalLM.from_pretrained(real_name,low_cpu_mem_usage=True)
        parallelize(model, num_gpus=2, fp16=True, verbose='detail')
        tokenizer = AutoTokenizer.from_pretrained(real_name)
        model_dict[call_name+'_model'] = model
        model_dict[call_name+'_tokenizer'] = tokenizer

    return model_dict



"""
def infer(context, top_p=0.9, temp=1.0, gen_len=512):
    tokens = tokenizer.encode(context)

    provided_ctx = len(tokens)
    pad_amount = seq - provided_ctx

    padded_tokens = np.pad(tokens, ((pad_amount, 0),)).astype(np.uint32)
    batched_tokens = np.array([padded_tokens] * total_batch)
    length = np.ones(total_batch, dtype=np.uint32) * len(tokens)

    start = time.time()
    output = network.generate(batched_tokens, length, gen_len, {"top_p": np.ones(total_batch) * top_p, "temp": np.ones(total_batch) * temp})

    samples = []
    decoded_tokens = output[1][0]

    for o in decoded_tokens[:, :, 0]:
      samples.append(f"\033[1m{context}\033[0m{tokenizer.decode(o)}")

    print(f"completion done in {time.time() - start:06}s")
    return samples

print(infer("EleutherAI is")[0])

"""

def GenerateText(text,tokens):
    
 
    if len(model_dict) == 2:
        model_name = 'gpt-j'

    start_time = time.time()
   

    model = model_dict[model_name + '_model']
    tokenizer = model_dict[model_name + '_tokenizer']
        
    generator = pipeline('text-generation',  model=model, tokenizer=tokenizer)
    # First Test -> Quechua   
    #output = generator(text,  top_p=1, top_k=12, length_penalty=0, do_sample=True, temperature=1.33, max_new_tokens=tokens)
    
    
    """generate text with hyperparameters
        "frequencyPenalty": 0,
        "logprobsState": "off",
        "maxTokens": 292,
        "model": "gpt-j-6b",
        "presencePenalty": 0,
        "tailFreeSampling": 0.8200000000000001,
        "temperature": 1.72,
        "topK": 83,
        "topP": 0.8200000000000001
    Returns:
        _type_: array
    """
    output = generator(text, max_new_tokens=tokens, no_repeat_ngram_size=2,num_return_sequences=3,num_beams=5)

    end_time = time.time()

    full_output = output
    output = output[0]['generated_text']
    result = {'inference_time': end_time - start_time,
              'result': output,
              'full_output': full_output
              }
    return result
def extractArgumentsFromJson(jsonString):
    loadedJson =json.loads(jsonString)
    return dict(loadedJson)

def GenerateTextByPayload(payload):
    
 



    if len(model_dict) == 2:
        model_name = 'gpt-j'

    start_time = time.time()
   

    model = model_dict[model_name + '_model']
    tokenizer = model_dict[model_name + '_tokenizer']
        
    generator = pipeline('text-generation',  model=model, tokenizer=tokenizer)
    # First Test -> Quechua   
    #output = generator(text,  top_p=1, top_k=12, length_penalty=0, do_sample=True, temperature=1.33, max_new_tokens=tokens)
    
    
    """generate text with hyperparameters
        "frequencyPenalty": 0,
        "logprobsState": "off",
        "maxTokens": 292,
        "model": "gpt-j-6b",
        "presencePenalty": 0,
        "tailFreeSampling": 0.8200000000000001,
        "temperature": 1.72,
        "topK": 83,
        "topP": 0.8200000000000001
    Returns:
        _type_: array
    """
    
    payloadArguments = extractArgumentsFromJson(payload)
    output = generator(payloadArguments)

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

@app.get("/inference")
async def inference(payload: dict = Body(...)):
    """
        max_new_tokens=payload.tokens, no_repeat_ngram_size=2,num_return_sequences=3,num_beams=5    
    """
    return GenerateTextByPayload(payload)