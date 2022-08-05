import os
import torch
 
import time
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from flores200_codes import flores_codes
from fastapi import FastAPI

def load_models():
    # build model and tokenizer
    model_name_dict = {
		  #'nllb-distilled-600M': 'facebook/nllb-200-distilled-600M',
                  #'nllb-1.3B': 'facebook/nllb-200-1.3B',
                  #'nllb-distilled-1.3B': 'facebook/nllb-200-distilled-1.3B',
                  'opus-mt-en-zh': 'Helsinki-NLP/opus-mt-en-zh'
                  #'nllb-3.3B': 'facebook/nllb-200-3.3B',
                  }

    model_dict = {}

    for call_name, real_name in model_name_dict.items():
        print('\tLoading model: %s' % call_name)
        model = AutoModelForSeq2SeqLM.from_pretrained(real_name)
        tokenizer = AutoTokenizer.from_pretrained(real_name)
        model_dict[call_name+'_model'] = model
        model_dict[call_name+'_tokenizer'] = tokenizer

    return model_dict


def translation(source, target, text):
    if len(model_dict) == 2:
        model_name = 'opus-mt-en-zh'

    start_time = time.time()
    source = flores_codes[source]
    target = flores_codes[target]

    model = model_dict[model_name + '_model']
    tokenizer = model_dict[model_name + '_tokenizer']

    translator = pipeline('translation', model=model, tokenizer=tokenizer, src_lang=source, tgt_lang=target)
    output = translator(text, max_length=400)

    end_time = time.time()

    full_output = output
    output = output[0]['translation_text']
    result = {'inference_time': end_time - start_time,
              'source': source,
              'target': target,
              'result': output,
              'full_output': full_output}
    return result

global model_dict
model_dict = load_models()

app = FastAPI()



@app.get("/")
async def root():
    return {"message": "run /translate?source=&target=&text="}

@app.get("/translate")
async def translate(source: str = "Portuguese", target: str = "English", text: str = 'loirinha rabuda'):
 
    return {
        "source":   source,
        "target":   target,
        "text": text,
        "translation": translation(source,target,text)}

 
