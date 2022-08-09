
# NLP Tests

Basic Tests for testing with natural language processing

Basic Natural language processing tasks using huggingface transformers 
Inference only
 








## Installation

Install required packages for inference 

First install miniconda env download at:
https://docs.conda.io/en/latest/miniconda.html#linux-installers
```bash
bash Miniconda3-py39_4.12.0-Linux-x86_64.sh

```

GPU

```bash
install pytorch 
conda install pytorch torchvision torchaudio cudatoolkit=11.6 -c pytorch -c conda-forge
```


CPU only

```bash
conda install pytorch torchvision torchaudio cpuonly -c pytorch
```


required pip packages
```bash

pip install transformers sentencepiece fastapi uvicorn

```
 


    
## Usage/Examples

usage examples, I tested them all in fastapi to speed up the inference without having to load the model again

```bash
                    file-name : program
uvicorn --port 5643  translate-nllb:app
uvicorn --port 5643  translate-mbart-en-pt:app
```

