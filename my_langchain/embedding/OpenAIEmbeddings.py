import openai

class OpenAIEmbeddingsClass:
    def __init__(self, openai_api_key):
        self.api_key = openai_api_key
        openai.api_key = self.api_key

    def embed(self, text):
        response = openai.Embedding.create(
            input=[text],
            model="text-embedding-ada-002"
        )
        return response['data'][0]['embedding']
