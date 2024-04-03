import sys
from dotenv import load_dotenv
from openai import OpenAI

class Conversation():
    def __init__(self, mode = None):
        self.mode = mode
        self.message_history = []

        # generates OpenAI client
        self.client = OpenAI()

    def get_user_message(self):
        try:
            user_message = input("Ingrese su consulta: ")

            if len(user_message) == 0:
                raise Exception("Error: La consulta no debe estar vacía.")

            print("You: " + user_message)
            return user_message
        except Exception as e:
            print(e)

    def get_chatGPT_message(self, user_message):
        try:
            response = self.client.chat.completions.create(
                # frequency_penalty = 0,
                # presence_penalty = 0
                # temperature = 1,
                # top_p = 1,
                max_tokens = 4096,
                messages = self.message_history + [
                    {
                        "role": "user",
                        "content": user_message
                    }
                ],
                model = "gpt-3.5-turbo-0125",
            )

            chatGPT_message = response.choices[0].message.content

            if self.mode == CONVERSATION:
                self.message_history.append({ "role": "user", "content": user_message })
                self.message_history.append({ "role": "assistant", "content": chatGPT_message })

            print("ChatGPT: " + chatGPT_message)
            return chatGPT_message
        except Exception as e:
            print(e)

    def get_message_history(self):
        return self.message_history

load_dotenv()

CONVERSATION = "conversation"
MODE = CONVERSATION if "--convers" in sys.argv else ""
conversation = Conversation(MODE)

def main():
    user_message = conversation.get_user_message()
    conversation.get_chatGPT_message(user_message)

if MODE == CONVERSATION:
    while True:
        main()
else:
    main()
