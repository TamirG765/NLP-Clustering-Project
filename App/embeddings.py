from transformers import GPT2Model, GPT2Tokenizer
import torch

def load_model_and_tokenizer():
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2Model.from_pretrained("gpt2")
    return tokenizer, model

def get_embeddings(texts, tokenizer, model):
    inputs = tokenizer(texts, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Take the mean of all token embeddings to get a single embedding vector per text
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()