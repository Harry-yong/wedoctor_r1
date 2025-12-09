#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2025/03/11 10:30:53
@Author  :   yangqinglin
@Version :   v1.0
@Email   :   yangql1@wedoctor.com
@Desc    :   None
'''

from datasets import load_dataset
import json
import jieba
from rank_bm25 import BM25Okapi
import re

# 示例文本
content = """<answer>
开放性气胸是指胸壁出现开放性伤口，使胸膜腔与外界大气相通，导致胸膜腔内负压消失。正常情况下，胸膜腔内的负压有助于维持肺的膨胀状态。当负压消失时，空气进入胸膜腔，压迫肺组织。

首先，**患侧肺会发生萎缩**。由于空气进入胸膜腔，肺组织受到压迫，无法正常扩张，导致肺泡通气减少。

其次，**呼吸功能减退**。肺的萎缩使得患侧的通气和换气功能大大降低，导致机体获得的氧气减少，二氧化碳排出受阻，可能引起低氧血症和二氧化碳潴留。

此外，空气通过胸壁伤口进出，可能引起**纵隔摆动**，影响心脏和大血管的正常功能，进一步加重呼吸和循环系统的紊乱。

综上所述，开放性气胸引起的病理生理紊乱主要表现为**患侧肺萎缩，呼吸功能减退**。
</answer>"""
text2 = "关节炎"
pattern = r"<answer>\s*(.*?)\s*</answer>"
test = re.search(pattern, content, re.DOTALL).group(1)
print(test)

# pattern = r'<answer>\s*(.*?)\s*</answer>'
# matches = re.search(pattern, text1).group(1)
# print(matches)
# # 分词
# tokenized_text1 = list(jieba.cut(matches))
# tokenized_text2 = list(jieba.cut(text2))
# intersection = set(tokenized_text1).intersection(set(tokenized_text2))
# print(tokenized_text1)
# print(len(set(intersection))/len(set(tokenized_text1)))
# print(intersection)

# print(tokenized_text1, tokenized_text2)

# dataset = load_dataset("json", data_files=["/data4/wedoctor/yangqinglin/wedoctor_r1/data/Citrus_S3.json"],split="train")
# train, test = dataset.train_test_split(test_size=0.2).values()
# print(train, test)
# print(dataset)
# def change_input(file):
    
#     with open(file, "r") as f:
#         # data = json.load(f)
#         data = [json.loads(line) for line in f]
#     with open("wedoctor_r1/data/wedoctor_20250312.json", "a+") as out_f:
#         for item in data:
#             s = {"input": item["input"], "output": item["output"]}
#             out_f.write(json.dumps(s, ensure_ascii=False) + "\n")
#             # pattern = r"<Question>(.*?)</Question>"
#             # match = re.search(pattern, item["input"], re.DOTALL)
#             # question_content = match.group(1).strip()
#             # print(question_content)

# if __name__ == '__main__':
#     file = "/data4/wedoctor/yangqinglin/wedoctor_r1/data/wedoctor_20250311.json"
#     change_input(file)
# dev的提交：12093
