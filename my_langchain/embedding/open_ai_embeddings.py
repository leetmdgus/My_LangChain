import os
import openai

class OpenAIEmbeddings:
    def __init__(self):
        pass
    
    def embed_texts(self, text:str):        
        response = openai.Embedding.create(
            model="text-embedding-ada-002",
            input = text
        )

        return response['data'][0]['embedding']
        
