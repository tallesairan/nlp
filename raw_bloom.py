# pip install -q transformers
from transformers import AutoModelForCausalLM, AutoTokenizer

checkpoint = "bigscience/bloomz-7b1-mt"

print("Loading model: %s" % checkpoint)
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint)
print("Model loaded")
inputs = tokenizer.encode("Generate 30 pharses about: true love", return_tensors="pt")
print("Generating...")
outputs = model.generate(inputs, max_length=512, do_sample=True, top_k=50, top_p=0.95,  temperature=1.0, repetition_penalty=1.0, length_penalty=1.0, num_beams=1, early_stopping=True, no_repeat_ngram_size=3, bad_words_ids=None, decoder_start_token_id=None, use_cache=True)
print(tokenizer.decode(outputs[0]))