import openai
import os

API_KEY = 'PASTE_YOUR_API_KEY_HERE'
openai.api_key = API_KEY

model_id = 'gpt-4'
gpt = openai.Model(model_id)


def chatgpt_conversation(conversation_log):
    response = openai.ChatCompletion.create(
        model = model_id,
        messages = conversation_log
    )
    print(response)
    conversation_log.append({'role': response.choices[0].message.role,
                             'content': response.choices[0].message.content.strip()
    })
    return conversation_log

conversations = []
#system, user, assistant
conversations.append({'role': 'system', 'content': 'How may I help you?'})

conversations = chatgpt_conversation(conversations)

while True:
    prompt = input('User:')
    conversations.append({'role': 'user', 'content': prompt})
    conversations = chatgpt_conversation(conversations)
    print(conversations)
