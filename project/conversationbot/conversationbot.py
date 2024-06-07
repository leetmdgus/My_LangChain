from My_LangChain.my_langchain.chat_models import MyOpenAI
from My_LangChain.my_langchain.memory import ConversationSummaryMemory
from My_LangChain.my_langchain.chains import ConversationChain
from My_LangChain.my_langchain.vectorstores import Chroma

class ConversationBot:
    def __init__(self):
        llm = MyOpenAI()
        retriver = None
        memory = ConversationSummaryMemory(llm)
        self.chain = ConversationChain.from_llm(llm=llm, memory=memory,retriver=retriver)
    
    def conversation(self, txt):
        return self.chain(txt)
    
    # def clear(self):
    #     self()