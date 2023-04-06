import jieba
import re

def split_sentences(text):
    # 使用正则表达式分割句子
    pattern = r'[\。\！\？\；\，\!\?\;\,\n]'
    sentences = re.split(pattern, text)
    
    # 遍历分割后的列表，将连续的句子合并成一个句子
    result = []
    tmp = ''
    for sentence in sentences:
        if sentence != '':
            tmp += sentence
            # 使用jieba分词判断是否到达句子结尾
            if len(jieba.lcut(tmp)[-1]) == 1:
                result.append(tmp)
                tmp = ''
    
    # 如果最后还有剩余的句子，则将其添加到列表中
    if len(tmp) > 0:
        result.append(tmp)
    
    return result

# print(split_sentences('早安！今天天气真好，早饭吃什么？'))