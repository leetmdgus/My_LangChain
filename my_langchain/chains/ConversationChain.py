from My_LangChain.my_langchain.openai_api_key import OPENAI_KEY
OPENAI_API_KEY = OPENAI_KEY().OPENAI_API_KEY;

from My_LangChain.my_langchain.chat_models.ChatOpenAI import ChatOpenAIClass


class ConversationChain:
    def __init__(self, llm):
        self.llm = ChatOpenAIClass(openai_api_key=OPENAI_API_KEY);
    def run(self, str):
        pass
    def __str__(self):
        pass