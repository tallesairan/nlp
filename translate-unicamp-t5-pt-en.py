import os
import torch
 
import time
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from flores200_codes import flores_codes
from fastapi import FastAPI

def load_models():
    # build model and tokenizer
    model_name_dict = {
		          'translation': 'unicamp-dl/translation-pt-en-t5',
                  #'nllb-1.3B': 'facebook/nllb-200-1.3B',
                  #'translation': 'facebook/nllb-200-distilled-1.3B',
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
        model_name = 'translation'

    start_time = time.time()
    

    model = model_dict[model_name + '_model']
    tokenizer = model_dict[model_name + '_tokenizer']

    translator = pipeline('translation', model=model, num_workers=54, tokenizer=tokenizer)
    output = translator(text, max_length=512)

    end_time = time.time()

    full_output = output
    output = output[0]['translation_text']
    result = {'time': end_time - start_time,
              'text': text,
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
async def translate(source: str = "Portuguese", target: str = "English", text: str = 'Good day'):
 
    return translation(source,target,text)

 
