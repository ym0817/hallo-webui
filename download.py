import torch
from modelscope import snapshot_download   #, AutoTokenizer#  AutoModel,
import os
# model_dir = snapshot_download('qwen/Qwen2-7B-Instruct', cache_dir='./', revision='master')

# model_dir = snapshot_download('qwen/Qwen2-0.5B-Instruct', cache_dir='./', revision='master')

# model_dir = snapshot_download('qwen/Qwen2-14B', cache_dir='./', revision='master')

model_dir = snapshot_download('fudan-generative-vision/Hallo', cache_dir='./' )



