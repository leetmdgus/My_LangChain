

class Chroma:
    def __init__(self, texts):
        self.texts = texts

    @classmethod
    def from_texts(cls, texts):
        return cls(texts)
    
    def as_retriever(self):
        combine = '';
        for text in self.texts:
            combine += text
            
        txt = '미리 주어진 데이터는 다음과 같아.' + combine + '이것을 대답에 근거로해서 대답해줘.'
        return txt



if __name__ == '__main__':
    from My_LangChain.my_langchain.chat_models import MyOpenAI
    from My_LangChain.my_langchain.chains import LLMChain
    
    texts = ['사과는 맛있다. ', '영희는 사과를 좋아한다. ', '철수도 사과를 좋아한다. ', '모두가 사과를 좋아하는 것은 아니다. ', '민수는 사과를 좋아하지 않는다.']
    vectorestore = Chroma.from_texts(texts)
    retriever = vectorestore.as_retriever()
    
    llm = MyOpenAI()
    chain = LLMChain.from_llm(llm=llm, retriever=retriever)
    
    print(chain('사과를 싫어하는 사람과 사과를 좋아하는 사람을 각각 말해줘'))
    