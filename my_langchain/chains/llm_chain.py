from my_langchain.chat_models import ChatOpenAI

class LLMChain:
    def __init__(self, llm: ChatOpenAI, retriever=[]):
        self.llm = llm
        self.retriever = retriever
    
    @classmethod
    def from_llm(cls, llm, retriever):
        return cls(llm, retriever)
    
    def __call__(self, query: str):
        answer_list = [self.llm.predict(f'{r}는 관련 자료야. 이것만을 참고하여 {query}를 답해줘') for r in self.retriever]
        query = f'{answer_list}중에 사용자가 원할만한 답을 선택하고, 그것만을 말 해'
        response = self.llm.predict(query)
        return response