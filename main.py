import re

with open("the-verdict.txt", "r", encoding="utf-8" ) as file:
    raw_text = file.read()
print("Total number of characters in the text: ", len(raw_text))
print(raw_text[:99]) #Print the first 100 characters of the text

tokens = re.split(r'[,.:;?_!"()\']|--|\s', raw_text)
print("Total number of tokens in the text first strip: ", len(tokens))
tokens = [item for item in tokens if item.strip()] # Remove empty tokens
print("Total number of tokens in the text: ", len(tokens))
print(tokens[:30]) #Print the first 30 tokens of the text

unique_tokens = sorted(set(tokens)) # Get unique tokens and sort them
print("Total number of unique tokens in the text: ", len(unique_tokens))
print(unique_tokens[:30]) #Print the first 30 unique tokens of the text

vocabulary = {token: index for index, token in enumerate(unique_tokens)} # Create a vocabulary mapping
for i, item in enumerate(vocabulary.items()):
    print(item) #Print the first 30 items of the vocabulary
    if i > 30:
        break

