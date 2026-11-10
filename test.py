import ollama

response = ollama.chat(
    model='gemma4',
    messages=[
        {
            'role': 'user',
            'content': 'Who are you?'
        }
    ]
)

print(response['message']['content'])