file_path = './recipes.txt'
output_file = 'my_fav_recipes.txt'
textFromFile = ""

try:
    with open(file_path, 'r') as file:
        textFromFile = file.read()
    print("File content loaded successfully.")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

print(textFromFile)

from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama2",
    temperature=0,
)


messages = [
    (
        "system",
        "You are a highly skilled assistant designed to analyze text containing multiple unorganised recipe details from random social media posts. DON'T put any extra word communicating with me. Just give the filtered answer. Your task is to extract the names of the recipes and organize their details clearly. Present your response in a structured format, where each recipe has its own section. Use the recipe name as the heading for each section, followed by its details in a concise and readable paragraph.",
    ),
    ("human", textFromFile),
]
ai_msg = llm.invoke(messages)
print(ai_msg.content)

try:
    # Write the categorized list to the output file
    with open(output_file, "w") as f:
        f.write(ai_msg.content.strip())

    print(f"Categorized grocery list has been saved to '{output_file}'.")
except Exception as e:
    print("An error occurred:", str(e))