from My_LangChain.my_langchain.memory import ConversationBufferMemory
from My_LangChain.my_langchain.chat_models.ChatOpenAI import ChatOpenAIClass

class ConversationalRetrievalChainClass:
    def __init__(self, llm:ChatOpenAIClass, retriever, memory:ConversationBufferMemory):
        self.llm = llm
        self.retriever = retriever
        self.memory = memory

    @classmethod
    def from_llm(cls, llm, retriever, memory:ConversationBufferMemory):
        return cls(llm, retriever, memory)

    def __call__(self, input:str):
        self.memory.add_message(input)
        documents = self.retriever.retrieve(self.llm.embed(input))
        response = self.llm.generate_response(input)
        self.memory.add_message(response)
        return response
