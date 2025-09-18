 from transformers import BertForSequenceClassification, Trainer, TrainingArguments, BertTokenizer
from datasets import load_dataset

# Load dataset and tokenizer
dataset = load_dataset("imdb", split="train[:2000]")
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

def tokenize(batch):
    return tokenizer(batch["text"], padding=True, truncation=True, max_length=128)

dataset = dataset.map(tokenize, batched=True)
dataset = dataset.rename_column("label", "labels")
dataset.set_format(type="torch", columns=["input_ids", "attention_mask", "labels"])

# Load model
model = BertForSequenceClassification.from_pretrained("bert-base-uncased")

# Training arguments
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=1,
    per_device_train_batch_size=8,
    logging_steps=10,
    save_steps=50,
    evaluation_strategy="no"
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset
)

trainer.train()
print("Fine-tuning complete!")
