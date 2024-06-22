from my_langchain.chat_models import ChatOpenAI

class LLMChain:
    def __init__(self, llm:ChatOpenAI, retriver = None):
        self.llm:ChatOpenAI = llm
        self.retriver = retriver
    
    @classmethod
    def from_llm(cls, llm, retriver):
        return cls(llm, retriver)
    
    def __call__(self, prompt: str):
        response = self.llm.predict(prompt)
        return response
