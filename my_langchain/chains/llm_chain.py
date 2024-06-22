from my_langchain.chat_models import ChatOpenAI

class LLMChain:
    def __init__(self, llm:ChatOpenAI, retriver):
        self.llm:ChatOpenAI = llm
        self.retriver = retriver
    
    @classmethod
    def from_llm(cls, llm, retriver):
        return cls(llm, retriver)
    
    def __call__(self, query: str):
        query = f'{self.retriver}만을 참고해서 {query}를 답해줘'
        return self.llm.predict(query)