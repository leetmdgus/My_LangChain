from openai import OpenAI;
from my_langchain.schema import (
    HumanMessage,
)

class ChatOpenAI:
    def __init__(self):
        self.client = OpenAI()   
    
    def predict(self, text:str, messages:list = None):
        if messages == None:
            messages = [HumanMessage(text).message]
        else:
            messages.append(HumanMessage(text).message)

        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages= messages,
        )
        return completion.choices[0].message.content
    

