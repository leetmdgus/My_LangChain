from My_LangChain.my_langchain.chat_models import MyOpenAI

class LLMChain:
    def __init__(self, llm, retriever):
        self.llm = llm
        self.retriever = retriever
    
    @classmethod
    def from_llm(cls, llm, retriever):
        return cls(llm, retriever)
    
    def __call__(self, input: str):
        prompt = self.retriever + input
        response = self.llm.predict(prompt)
        return response

if __name__ == '__main__':
    llm = MyOpenAI()
    retriever = None
    
    chain = LLMChain.from_llm(llm=llm, retriever=retriever)

    
    
