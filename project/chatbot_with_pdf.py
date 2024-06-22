from my_langchain.chains.llm_chain import LLMChain
from my_langchain.text_splitter import CharacterTextSplitter
from my_langchain.document_loaders import PyPDFLoader

from my_langchain.vectorstores import Chroma
from my_langchain.chat_models import ChatOpenAI
from my_langchain.memory import ConversationBufferMemory
from my_langchain.chains import ConversationChain


class ChatbotWithPDF:
    def __init__(self, pdf: str):
        llm = ChatOpenAI();
        
        loader = PyPDFLoader(pdf)
        pages = loader.load()

        text_splitter = CharacterTextSplitter(chunk_size=500)
        splits = text_splitter.split_text(pages)

        vectorestore = Chroma.from_texts(texts=splits)
        retriver = vectorestore.as_retriever()
        
        self.qa = LLMChain.from_llm(llm = llm, retriver=retriver)
        
    def __call__(self, input: str):
        print(self.qa(input))


if __name__ == '__main__':
    chat = ChatbotWithPDF(pdf = "https://snuac.snu.ac.kr/2015_snuac/wp-content/uploads/2015/07/asiabrief_3-26.pdf")

    print('첫 번째 질문')
    chat('저출산을 극복한 나라들은 어디가 있어?')
    print('두 번째 질문')
    chat('최신 관련 자료들의 문헌 제목을 알려줘')
