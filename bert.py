from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')


tokens = tokenizer.encode('This is amazing, I loved it. Great!', return_tensors='pt')
result = model(tokens)
print(int(torch.argmax(result.logits))+1)

# 5

tokens = tokenizer.encode('It was good but could been better.', return_tensors='pt')
result = model(tokens)
print(int(torch.argmax(result.logits))+1)

# 3

tokens = tokenizer.encode('徐静真好看！', return_tensors='pt')
result = model(tokens)
print(int(torch.argmax(result.logits))+1)

#5

tokens = tokenizer.encode('今天真糟糕!!!!!', return_tensors='pt')
result = model(tokens)
print(int(torch.argmax(result.logits))+1)

#1

