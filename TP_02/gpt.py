"""
Module that generates a conversation between a user and ChatGPT.
"""

import sys
from dotenv import load_dotenv
from openai import OpenAI

class Conversation():
    """
    Conversation class that has the necessary methods to use the OpenAI's API and manage the history of messages

    Args:
        mode (str, optional): if it is "CONVERSATION" the class will use all history of messages to make the requests.
    """
    def __init__(self, mode = None):
        self.mode = mode
        self.message_history = []

        # generates OpenAI client
        self.client = OpenAI()

    def get_user_message(self):
        """
        Asks the user for the message and prints it with "You: " before it.

        Returns:
            str: the user message.

        Raises:
            ValueError: if the message is empty
        """
        try:
            user_message = input("Ingrese su consulta: ")

            if len(user_message) == 0:
                raise ValueError("Error: La consulta no debe estar vacía.")

            print("You: " + user_message)
            return user_message
        except ValueError as e:
            print(e)
            return None

    def get_chatgpt_message(self, user_message):
        """
        Generate a response for the user message with OpenAI's API.

        Args:
            user_message (str): user message to be used in the request.

        Returns:
            str: message from the response.
        """
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

            chatgpt_message = response.choices[0].message.content

            if self.mode == CONVERSATION:
                self.message_history.append({ "role": "user", "content": user_message })
                self.message_history.append({ "role": "assistant", "content": chatgpt_message })

            print("ChatGPT: " + chatgpt_message)
            return chatgpt_message
        except ValueError as e:
            print(e)
            return None

    def get_message_history(self):
        """
        Obtains and returns the message history.

        Returns:
            list: history of messages.
        """
        return self.message_history

load_dotenv()

CONVERSATION = "conversation"
MODE = CONVERSATION if "--convers" in sys.argv else ""
conversation = Conversation(MODE)

def main():
    """
    Executes the necessary methods to make the program work.
    """
    user_message = conversation.get_user_message()
    conversation.get_chatgpt_message(user_message)

if MODE == CONVERSATION:
    while True:
        main()
else:
    main()
