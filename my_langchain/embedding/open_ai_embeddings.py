import os
import openai
from My_LangChain.my_langchain.openai_api_key import OPENAI_KEY

class OpenAIEmbeddings:
    def __init__(self):
        # self.client = openai(openai_api_key = OPENAI_KEY().OPENAI_API_KEY);
        pass
    
    def embed_texts(self, text:str):        
        response = openai.Embedding.create(
            model="text-embedding-ada-002",
            input = text
        )

        return response['data'][0]['embedding']
        

if __name__ == '__main__':
    text = '123'
    embedding = OpenAIEmbeddings()
    print(embedding.embed_texts(text))