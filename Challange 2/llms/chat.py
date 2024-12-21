from langchain_ollama import ChatOllama
import requests

llm = ChatOllama(
    model="llama2",
    temperature=0,
)

from langchain.schema import AIMessage, HumanMessage, SystemMessage

chat_history = []  # Use a list to store messages

response = requests.get('https://localhost:8000/api/ingredients/get-ingredients')
avaliable_ingredients = response.data

system_message = SystemMessage(content=f"You are a helpful assistant that suggests recipes on basis of Avaliable Ingredients and favourite recipes. Avaliable Ingredients are: {avaliable_ingredients}")
chat_history.append(system_message)  # Add system message to chat history

# Chat loop
while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query))  # Add user message

    result = llm.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))  

    print(f"AI: {response}")


# print("---- Message History ----")
# print(chat_history)