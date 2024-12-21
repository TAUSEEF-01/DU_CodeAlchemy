# train_model.py

from transformers import MBartForConditionalGeneration, MBartTokenizer, Seq2SeqTrainingArguments, Seq2SeqTrainer

def train_model(train_data, val_data, model_name="facebook/mbart-large-50", output_dir="./results"):
    tokenizer = MBartTokenizer.from_pretrained(model_name)
    model = MBartForConditionalGeneration.from_pretrained(model_name)

    training_args = Seq2SeqTrainingArguments(
        output_dir=output_dir,
        evaluation_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=16,
        num_train_epochs=3,
        weight_decay=0.01,
        save_total_limit=2,
        predict_with_generate=True,
        logging_dir="./logs",
    )

    trainer = Seq2SeqTrainer(
        model=model,
        args=training_args,
        train_dataset=train_data,
        eval_dataset=val_data,
        tokenizer=tokenizer,
    )

    trainer.train()
    trainer.save_model(output_dir)
    # Save the model
    
    model.save_pretrained("./banglish_to_bengali_model")
    tokenizer.save_pretrained("./banglish_to_bengali_model")

if __name__ == "__main__":
    from preprocess_data import preprocess_data
    from load_data import load_and_split_data

    train_data, val_data = load_and_split_data()
    tokenized_train_data, tokenized_val_data = preprocess_data(train_data, val_data)
    train_model(tokenized_train_data, tokenized_val_data)




# from transformers import T5ForConditionalGeneration, T5Tokenizer, Trainer, TrainingArguments
# from datasets import load_dataset
# from load_data import load_and_split_data  # Replace with your actual data loading function

# # Load and preprocess data
# train_data, val_data = load_and_split_data()  # Assuming this function loads and splits the data

# # Load pre-trained model and tokenizer
# model_name = "t5-small"
# model = T5ForConditionalGeneration.from_pretrained(model_name)
# tokenizer = T5Tokenizer.from_pretrained(model_name)

# # Tokenize data
# def tokenize_function(examples):
#     return tokenizer(examples['rm'], padding="max_length", truncation=True, max_length=128)

# train_data = train_data.map(tokenize_function, batched=True)
# val_data = val_data.map(tokenize_function, batched=True)

# # Prepare training arguments
# training_args = TrainingArguments(
#     output_dir="./banglish_to_bengali_model",  # Save model here after training
#     evaluation_strategy="epoch",
#     learning_rate=2e-5,
#     per_device_train_batch_size=16,
#     per_device_eval_batch_size=16,
#     num_train_epochs=3,
#     weight_decay=0.01,
# )

# # Initialize Trainer
# trainer = Trainer(
#     model=model,
#     args=training_args,
#     train_dataset=train_data,
#     eval_dataset=val_data,
# )

# # Train the model
# trainer.train()

# # Save the model
# model.save_pretrained("./banglish_to_bengali_model")
# tokenizer.save_pretrained("./banglish_to_bengali_model")




# import os
# from datasets import load_dataset
# from transformers import T5Tokenizer, T5ForConditionalGeneration, Trainer, TrainingArguments
# from sklearn.model_selection import train_test_split
# import torch

# # Load the dataset (replace this with your dataset loading step)
# # Assuming the dataset is in a CSV or JSON file, adjust accordingly
# dataset = load_dataset("SKNahin/bengali-transliteration-data")
# print(dataset)

# # Load the pre-trained tokenizer
# tokenizer = T5Tokenizer.from_pretrained("t5-small")

# # Define the preprocessing function
# def preprocess_function(examples):
#     # Tokenize the input and target (source and target texts)
#     inputs = tokenizer(examples['bn'], padding="max_length", truncation=True, max_length=128)
#     labels = tokenizer(examples['rm'], padding="max_length", truncation=True, max_length=128)
    
#     # The T5 model requires the labels in 'input_ids'
#     inputs['labels'] = labels['input_ids']
#     return inputs

# # Apply the preprocessing function to the dataset
# tokenized_train_data = dataset['train'].map(preprocess_function, batched=True)
# tokenized_val_data = dataset['validation'].map(preprocess_function, batched=True)

# # Ensure that the datasets are in the correct format
# tokenized_train_data.set_format(type='torch', columns=['input_ids', 'attention_mask', 'labels'])
# tokenized_val_data.set_format(type='torch', columns=['input_ids', 'attention_mask', 'labels'])

# # Load the pre-trained model
# model = T5ForConditionalGeneration.from_pretrained("t5-small")

# # Define training arguments
# training_args = TrainingArguments(
#     output_dir='./results',          # Output directory for model and logs
#     evaluation_strategy="epoch",     # Evaluate at the end of each epoch
#     learning_rate=2e-5,              # Learning rate
#     per_device_train_batch_size=8,   # Batch size per device during training
#     per_device_eval_batch_size=8,    # Batch size per device during evaluation
#     num_train_epochs=3,              # Total number of training epochs
#     weight_decay=0.01,               # Strength of weight decay
#     logging_dir='./logs',            # Directory for storing logs
#     logging_steps=10,                # Log every 10 steps
#     save_steps=500,                  # Save model checkpoint every 500 steps
#     load_best_model_at_end=True,     # Load the best model when finished
#     metric_for_best_model="accuracy",  # Metric to track the best model
# )

# # Define a simple metric for evaluation (accuracy or others based on your need)
# from datasets import load_metric

# metric = load_metric("accuracy")

# def compute_metrics(p):
#     predictions, labels = p
#     predictions = torch.argmax(predictions, dim=-1)
#     return metric.compute(predictions=predictions, references=labels)

# # Initialize the Trainer
# trainer = Trainer(
#     model=model,                         # The model to be trained
#     args=training_args,                  # Training arguments
#     train_dataset=tokenized_train_data,   # Training dataset
#     eval_dataset=tokenized_val_data,     # Validation dataset
#     compute_metrics=compute_metrics,     # Function to compute evaluation metrics
# )

# # Train the model
# trainer.train()

# # Save the model
# trainer.save_model("./banglish_to_bengali_model")
