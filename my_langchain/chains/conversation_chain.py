from My_LangChain.my_langchain.chat_models import MyOpenAI
from My_LangChain.my_langchain.memory import ConversationSummaryMemory
from My_LangChain.my_langchain.vectorstores import Chroma

class ConversationChain:
    def __init__(self, llm, memory, retriver = None):
        self.llm = llm
        self.retriver = retriver
        self.memory = memory
    
    @classmethod
    def from_llm(cls, llm, memory, retriver):
        return cls(llm, memory, retriver)
    
    def __call__(self, input: str):
        history = self.memory.get_history()
        
        prompt = '앞의 내용에서 사용자가' + history[0] + "라고 말한 걸 유의하며 답해주십시오. 이 문장은 다시 언급해서는 안됩니다."
        prompt += input
        
        prevData = ''
        if(self.retriver != None):
            prevData = self.retriver
            
        response = self.llm.predict(prevData+prompt)
        self.memory.add_history(prompt, response)
        return response

if __name__ == '__main__':
    llm = MyOpenAI()
    retriver = None
    memory = ConversationSummaryMemory(llm)
    
    chain = ConversationChain.from_llm(llm=llm, memory=memory, retriver=retriver)
    
    print('1')
    prompt = '나는 이렇게 비가 오는 날을 좋아해'
    print(prompt)
    print(chain(prompt))
    
    print('2')
    prompt = '그것보다 떡볶이 먹고 싶다.'
    print(prompt)
    print(chain(prompt))
    
    print('3')
    prompt = '아참, 내가 좋아하는 날이 화창한 날이라고 했던가?'
    print(prompt)
    print(chain(prompt))
