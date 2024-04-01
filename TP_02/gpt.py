import sys
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

CONVERSATION = "conversation"
MODE = CONVERSATION if "--convers" in sys.argv else ""
conversation = []

# generate OpenAI client
client = OpenAI()

def request(user_message, conversation = None):
    if conversation is None:
        conversation = []

    messages = conversation + [
        {
            "role": "user",
            "content": user_message
        }
    ]

    response = client.chat.completions.create(
        # frequency_penalty = 0,
        # presence_penalty = 0
        # temperature = 1,
        # top_p = 1,
        max_tokens = 4096,
        messages = messages,
        MODEl = "gpt-3.5-turbo-0125",
    )

    return response

def main():
    while True:
        try:
            user_message = input("Ingrese su consulta: ")

            if len(user_message) == 0:
                raise Exception("Error: La consulta no debe estar vacía")

            if MODE == CONVERSATION:
                conversation.append({ "role": "user", "content": user_message })

            print("You: " + user_message)

            response = request(user_message, conversation)

            if MODE == CONVERSATION:
                conversation.append(response.choices[0].message)

            print("ChatGPT: " + response.choices[0].message.content)
        except Exception as e:
            print(e)

main()
