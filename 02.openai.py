from openai import OpenAI

client = OpenAI(
    api_key="API_KEY"
)
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {"role": "user", "content": 'you are a virtual assisstant named jarvis skilled in general tasks like chatgpt'},
        {'role': 'user', 'content': 'who is althlete of the year'}
    ]
)
print(completion.choices[0].message)