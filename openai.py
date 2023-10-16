import openai

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
api_key = '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'

def chat_with_gpt(prompt):
    openai.api_key = api_key

    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=150,  # Adjust as needed
            temperature=0.7,  # Adjust as needed
            top_p=1.0, 
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )

        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        chat_prompt = f"You: {user_input}\nAI:"

        response = chat_with_gpt(chat_prompt)
        print("AI:", response)
