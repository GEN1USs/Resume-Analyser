from transformers import BertForSequenceClassification, BertTokenizer
import torch
import pandas as pd

MODEL_NAME = "bert-base-uncased"

def load_data(csv_file):
    df = pd.read_csv(csv_file)
    return df["text"], df["label"]

def train_model(train_csv, save_path="models/bert_model"):
    texts, labels = load_data(train_csv)
    tokenizer = BertTokenizer.from_pretrained(MODEL_NAME)
    model = BertForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=3)

    # Tokenize
    encodings = tokenizer(list(texts), truncation=True, padding=True)
    inputs = torch.tensor(encodings["input_ids"])
    labels = torch.tensor(labels.values)

    # Simple training loop (example)
    model.train()
    optimizer = torch.optim.Adam(model.parameters(), lr=2e-5)

    for epoch in range(3):
        optimizer.zero_grad()
        outputs = model(inputs, labels=labels)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        print(f"Epoch {epoch} loss {loss}")

    model.save_pretrained(save_path)
    tokenizer.save_pretrained(save_path)

if __name__ == "__main__":
    train_model("data/resumes_labels.csv")