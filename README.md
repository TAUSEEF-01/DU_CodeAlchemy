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
   run local database by:
   ```bash
   mongod
   ```

2. **Run Ingredient Management API**:  
   Start the express server for managing ingredients.
   ```bash
   node ./Challange\ 2/server/src/index.js
   ```
3. **Install required Python packages using pip:**:  
   ```bash
   pip install -r ./Challange\ 2/llms/requirements.txt
   ```
3. **Run Recipe Retrieval System**:  
  
   ```bash
   python ./Challange\ 2/llms/recipe_creator.py
   ```

4. **Run Chatbot Integration**:  
   Launch the chatbot interface for recipe suggestions.
   ```bash
   python ./Challange\ 2/llms/chat.py
   ```

---

## Additional Notes for Challenge 2
- MongoDB local server has been used for database. You can change connection string from `Challange 2/server/src/db/connect.js`
- Dummy recipe data should be kept in `Challange 2/llms/recipes.txt`. Or, Change it from `Challange\ 2/llms/recipe_creator.py`

---

## API Documentation

### Ingredient Management API

**Route**: `/api/ingredients/get-ingredients`  
**Method**: `GET`  
**Description**: Retrieve all available ingredients.  

**Route**: `/api/ingredients/update-ingredient`  
**Method**: `GET`  
**Description**: update an ingredient.  
**Sample Payload**:
```json
{
  "name": "Tomato",
  "quantity": 3
}
```
**Route**: `/api/ingredients/add-ingredient`  
**Method**: `GET`  
**Description**: add an ingredient.  
**Sample Payload**:
```json
{
  "name": "Tomato",
  "quantity": 3,
   "unit" : "kg"
}
```
