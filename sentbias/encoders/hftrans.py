''' Functions for handling HuggingFace Transformers models '''

import transformers
import torch

def load_model(model_path):
    config = transformers.AutoConfig.from_pretrained(model_path)
    tokenizer = transformers.AutoTokenizer.from_pretrained(model_path)
    model = transformers.AutoModel.from_pretrained(model_path, config=config)
    model.eval()
    return model, tokenizer

def encode(model, tokenizer, texts):
    encs = {}
    for text in texts:
        tokenized = tokenizer.tokenize(text)
        indexed = tokenizer.convert_tokens_to_ids(tokenized)
        #segment_idxs = [0] * len(tokenized)
        tokens_tensor = torch.tensor([indexed])
        #segments_tensor = torch.tensor([segment_idxs])
        enc, _ = model(tokens_tensor)

        enc = enc[:, 0, :]  # extract the last rep of the first input
        encs[text] = enc.detach().view(-1).numpy()
    return encs
