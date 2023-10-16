import azureopenai
import sqlite3

api_key = '613e7dfed67c4d2e89d7cb3c3bc56e01'

conn = sqlite3.connect('C:\\Users\\a889578\\Downloads\\chinook.db')

cursor = conn.cursor()

def chat(prompt):
  """Chats with the user using Azure OpenAI and a SQLite database.

  Args:
    prompt: The prompt to send to Azure OpenAI.

  Returns:
    The response from Azure OpenAI.
  """

  try:
    client = azureopenai.Client(api_key)
    response = client.generate(
      model="text-davinci-002-azure",
      prompt=prompt,
      max_tokens=150,
      temperature=0.9,
      top_p=0.95,
      frequency_penalty=0.0,
      presence_penalty=0.0,
    )
    return response.text.strip()
  except Exception as e:
    print(f"Error calling Azure OpenAI API: {e}")
    return None

if __name__ == "__main__":
  print("Welcome to the AI chat!")
  while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
      break

    response = chat(user_input)
    if response is not None:
      print("AI:", response)
