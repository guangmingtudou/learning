from transformers import AutoTokenizer

sentence = "Hello World!"
tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
token_id = tokenizer(sentence).input_ids
print(token_id)