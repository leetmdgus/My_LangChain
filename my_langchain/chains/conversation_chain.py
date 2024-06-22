from my_langchain.chat_models import ChatOpenAI
from my_langchain.memory import ConversationBufferMemory

class ConversationChain:
    def __init__(self, llm:ChatOpenAI, memory:ConversationBufferMemory, retriver = None):
        self.llm:ChatOpenAI = llm
        self.retriver = retriver
        self.memory:ConversationBufferMemory = memory
    
    @classmethod
    def from_llm(cls, llm, memory, retriver):
        return cls(llm, memory, retriver)
    
    def __call__(self, prompt: str):
        response = self.llm.predict(prompt, self.memory.get_history())
        self.memory.add_history(prompt, response)
        return response
