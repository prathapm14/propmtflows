import openai
import openai_api

api_key = "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"
openai_api.api_key = api_key

completion = openai_api.Completion()
response = completion.create(engine="text-davinci-002", prompt="What is the meaning of life?")

print(response.choices[0].text.strip())
