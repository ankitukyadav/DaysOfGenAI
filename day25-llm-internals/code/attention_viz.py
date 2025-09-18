from transformers import BertTokenizer, BertModel
import torch
import matplotlib.pyplot as plt

# Load pre-trained model and tokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased", output_attentions=True)

sentence = "Transformers use attention to understand context."
inputs = tokenizer(sentence, return_tensors="pt")
outputs = model(**inputs)

# Get attention weights from the first layer and first head
attentions = outputs.attentions[0][0, 0].detach().numpy()

tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])
plt.matshow(attentions)
plt.xticks(range(len(tokens)), tokens, rotation=90)
plt.yticks(range(len(tokens)), tokens)
plt.colorbar()
plt.title("Attention Weights (Layer 1, Head 1)")
plt.show()
