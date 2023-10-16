import sqlite3

api_key = ''

conn = sqlite3.connect('C:\\Users\\a889578\\Downloads\\chinook.db')

cursor = conn.cursor()

def chat(prompt):
  """Chats with the user using a SQLite database.

  Args:
    prompt: The prompt to send to the database.

  Returns:
    The response from the database.
  """

  global cursor

  cursor.execute(f"SELECT response FROM chat_utterances WHERE prompt = '{prompt}'")
  response = cursor.fetchone()
  if response is not None:
    return response[0]
  else:
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
