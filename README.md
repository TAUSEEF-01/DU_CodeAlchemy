# Hackathon Challenges: Banglish-to-Bengali Transliteration & Mofa’s Kitchen Buddy

## Team Information
**Team Name**: [Insert Your Team Name Here]  
**Team Members**:  
- Member 1: Naimul Islam 
- Member 2: Md. Tauseef - Ur - Rahman
- Member 3: Anirban Roy Sourov
---

## Setup Environment

### Prerequisites
1. **Python**: Make sure Python 3.8 or later is installed.
2. **Virtual Environment (Optional)**: Use a virtual environment to manage dependencies.
3. **Git**: Ensure Git is installed for cloning the repository.
4. **Hugging Face CLI**: Install if required for uploading models.

### Dependencies
Install required Python packages using pip:
```bash
pip install -r requirements.txt
```
The `requirements.txt` includes:
- `torch`
- `transformers`
- `datasets`
- `pandas`
- `numpy`
- `fastapi`
- `uvicorn`
- `openai` (if using OpenAI’s API for chatbot)
- `Pillow` (for OCR functionality if implemented)

---

## Folder Structure
```
.
|-- Challenge_1/
|   |-- load_data.py
|   |-- preprocess_data.py
|   |-- train_model.py
|   
|
|-- Challenge_2/
|   |-- database_schema.sql
|   |-- ingredient_api.py
|   |-- recipe_retrieval.py
|   |-- chatbot_integration.py
|   |-- requirements.txt
|
|-- README.md
|-- requirements.txt
```

---

## How to Run the Scripts

### Challenge 1: Banglish-to-Bengali Transliteration
1. **Load Dataset**:  
   Run `load_data.py` to load and split the dataset.
   ```bash
   python Challenge_1/load_data.py
   ```

2. **Preprocess Data**:  
   Tokenize and clean the dataset.
   ```bash
   python Challenge_1/preprocess_data.py
   ```

3. **Train the Model**:  
   Fine-tune the selected pre-trained model on the dataset.
   ```bash
   python Challenge_1/train_model.py
   ```

4. **Upload Model**:  
   Use the Hugging Face CLI to upload the trained model, or share it using Git LFS if needed.
   ```bash
   huggingface-cli upload ./trained_model
   ```

### Challenge 2: Mofa’s Kitchen Buddy
1. **Setup Database**:  
   Create the database schema by running:
   ```bash
   sqlite3 kitchen.db < Challenge_2/database_schema.sql
   ```

2. **Run Ingredient Management API**:  
   Start the FastAPI server for managing ingredients.
   ```bash
   uvicorn Challenge_2.ingredient_api:app --reload
   ```

3. **Run Recipe Retrieval System**:  
   Parse recipe text and store it in the database.
   ```bash
   python Challenge_2/recipe_retrieval.py
   ```

4. **Run Chatbot Integration**:  
   Launch the chatbot interface for recipe suggestions.
   ```bash
   python Challenge_2/chatbot_integration.py
   ```

---

## Additional Notes
- Ensure all API endpoints are documented in the `API Documentation` section below.
- For Challenge 2, dummy recipe data can be modified in `recipe_retrieval.py`.

---

## API Documentation

### Ingredient Management API

**Route**: `/ingredients`  
**Method**: `GET`  
**Description**: Retrieve all available ingredients.  
**Sample Response**:
```json
[
  {
    "id": 1,
    "name": "Tomato",
    "quantity": 3
  },
  {
    "id": 2,
    "name": "Flour",
    "quantity": 500
  }
]
```

**Route**: `/ingredients`  
**Method**: `POST`  
**Description**: Add or update an ingredient.  
**Sample Payload**:
```json
{
  "name": "Tomato",
  "quantity": 3
}
```

### Recipe Retrieval API
**Route**: `/recipes`  
**Method**: `GET`  
**Description**: Retrieve recipes based on available ingredients.  
**Sample Response**:
```json
[
  {
    "name": "Tomato Soup",
    "ingredients": ["Tomato", "Salt", "Water"],
    "preparation_time": "30 minutes",
    "cuisine": "Italian"
  }
]
```

### Chatbot API
**Route**: `/chat`  
**Method**: `POST`  
**Description**: Interact with the chatbot for personalized recipe suggestions.  
**Sample Payload**:
```json
{
  "message": "I want something sweet."
}
```

**Sample Response**:
```json
{
  "response": "How about Chocolate Cake? You have most of the ingredients."
}
```

---

**Happy Hacking!**
