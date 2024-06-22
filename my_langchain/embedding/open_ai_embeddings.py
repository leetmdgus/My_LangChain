import os
import openai

class OpenAIEmbeddings:
    def __init__(self):
        pass
    
    @classmethod
    def text_embedding(cls, text) -> None:
        response = openai.Embedding.create(model="text-embedding-ada-002", input=text)
        return response["data"][0]["embedding"]
