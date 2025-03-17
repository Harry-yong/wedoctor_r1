#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   infer.py
@Time    :   2025/03/13 15:28:20
@Author  :   yangqinglin
@Version :   v1.0
@Email   :   yangql1@wedoctor.com
@Desc    :   None
'''
import torch
import transformers

from transformers import LlamaTokenizer, LlamaForCausalLM
from transformers import AutoTokenizer, AutoModelForCausalLM


generation_config = dict(
    temperature=0.7,
    top_k=40,
    top_p=0.9,
    do_sample=True,
    num_beams=1,
    repetition_penalty=1.0,
    # no_repeat_ngram_size=4,
    # encoder_no_repeat_ngram_size=4,
    max_new_tokens=1024
)

SYSTEM_PROMPT = """"""
question = """如何治疗糖尿病"""

model_path = "/data4/wedoctor/yangqinglin/wedoctor_r1/output/qwen2-0.5B-Instruct-grpo/checkpoint-1256"

tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

model = AutoModelForCausalLM.from_pretrained(
    model_path, 
    torch_dtype=torch.bfloat16,
    device_map='cuda:0',
    trust_remote_code=True,
)

messages = [
        {'role': 'system', 'content': SYSTEM_PROMPT},
        {'role': 'user', 'content': question},  # q1
    ]

text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

model_inputs = tokenizer([text], return_tensors="pt").to('cuda:0')
length = model_inputs.input_ids.shape[1]

generation_output = model.generate(
        input_ids = model_inputs.input_ids,
        **generation_config
    )



output_ids = generation_output.cpu().numpy()[0][length:].tolist()
output = tokenizer.decode(output_ids, skip_special_tokens=True)
print(output)