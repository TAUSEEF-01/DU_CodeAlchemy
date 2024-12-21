# # preprocess_data.py

# from transformers import T5Tokenizer
# from load_data import load_and_split_data

# def preprocess_data(train_data, val_data, model_name="t5-small"):
#     tokenizer = T5Tokenizer.from_pretrained(model_name)

#     # def preprocess_function(examples):
#     #     inputs = examples["banglish"]
#     #     targets = examples["bengali"]
#     #     model_inputs = tokenizer(inputs, max_length=128, truncation=True, padding="max_length")
#     #     labels = tokenizer(targets, max_length=128, truncation=True, padding="max_length")
#     #     model_inputs["labels"] = labels["input_ids"]
#     #     return model_inputs
    
    
#     def preprocess_function(examples):
#         inputs = examples["source"]  # Update to the correct column name
#         targets = examples["target"]  # Update to the correct column name
#         model_inputs = tokenizer(inputs, max_length=128, truncation=True, padding="max_length")
#         labels = tokenizer(targets, max_length=128, truncation=True, padding="max_length")
#         model_inputs["labels"] = labels["input_ids"]
#         return model_inputs


#     tokenized_train_data = train_data.map(preprocess_function, batched=True)
#     tokenized_val_data = val_data.map(preprocess_function, batched=True)

#     return tokenized_train_data, tokenized_val_data

# if __name__ == "__main__":
#     train_data, val_data = load_and_split_data()
#     tokenized_train_data, tokenized_val_data = preprocess_data(train_data, val_data)
#     print("Data preprocessing complete.")



# preprocess_data.py

from transformers import T5Tokenizer
from load_data import load_and_split_data

def preprocess_data(train_data, val_data, model_name="t5-small"):
    tokenizer = T5Tokenizer.from_pretrained(model_name)

    def preprocess_function(examples):
        inputs = examples["rm"]  # Updated to correct column name
        targets = examples["bn"]  # Updated to correct column name
        model_inputs = tokenizer(inputs, max_length=128, truncation=True, padding="max_length")
        labels = tokenizer(targets, max_length=128, truncation=True, padding="max_length")
        model_inputs["labels"] = labels["input_ids"]
        return model_inputs

    tokenized_train_data = train_data.map(preprocess_function, batched=True)
    tokenized_val_data = val_data.map(preprocess_function, batched=True)

    return tokenized_train_data, tokenized_val_data

if __name__ == "__main__":
    train_data, val_data = load_and_split_data()
    tokenized_train_data, tokenized_val_data = preprocess_data(train_data, val_data)
    print("Data preprocessing complete.")
