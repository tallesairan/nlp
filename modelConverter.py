
import os
from asyncio import threads
import torch
 
import time

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from flores200_codes import flores_codes
from fastapi import FastAPI

os.environ['KMP_DUPLICATE_LIB_OK']='True'

