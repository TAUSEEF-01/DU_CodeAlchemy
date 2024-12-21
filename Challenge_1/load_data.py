# # load_data.py

# from datasets import load_dataset

# def load_and_split_data():
#     dataset = load_dataset("SKNahin/bengali-transliteration-data")
#     dataset_split = dataset['train'].train_test_split(test_size=0.2, seed=42)
#     return dataset_split['train'], dataset_split['test']

# if __name__ == "__main__":
#     train_data, val_data = load_and_split_data()
#     print("Training samples:", len(train_data))
#     print("Validation samples:", len(val_data))



from datasets import load_dataset

def load_and_split_data():
    dataset = load_dataset("SKNahin/bengali-transliteration-data")
    print("Columns in the dataset:", dataset['train'].column_names)
    dataset_split = dataset['train'].train_test_split(test_size=0.2, seed=42)
    return dataset_split['train'], dataset_split['test']

if __name__ == "__main__":
    train_data, val_data = load_and_split_data()
    print("Training samples:", len(train_data))
    print("Validation samples:", len(val_data))
