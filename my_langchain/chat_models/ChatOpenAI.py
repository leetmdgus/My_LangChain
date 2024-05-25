import openai

class ChatOpenAIClass:
    def __init__(self, openai_api_key):
        self.api_key = openai_api_key
        openai.api_key = self.api_key

    def generate_response(self, prompt):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
