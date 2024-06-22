from my_langchain.chains.llm_chain import LLMChain
from my_langchain.text_splitter import RecursiveCharacterTextSplitter
from my_langchain.document_loaders import PyPDFLoader

from my_langchain.vectorstores import Chroma
from my_langchain.chat_models import ChatOpenAI


class ChatbotWithPDF:
    def __init__(self, pdf: str):
        self.llm = ChatOpenAI();
        
        loader = PyPDFLoader(pdf)
        pages = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=150)
        splits = text_splitter.split_text(pages)

        self.vectorestore = Chroma.from_texts(texts=splits)
        
    def __call__(self, query: str):
        doc = self.vectorestore.similarity_search(query)
        self.qa = LLMChain.from_llm(llm = self.llm, retriver=doc)
        print(self.qa(query))


if __name__ == '__main__':
    chat = ChatbotWithPDF(pdf = "https://snuac.snu.ac.kr/2015_snuac/wp-content/uploads/2015/07/asiabrief_3-26.pdf")

    print('첫 번째 질문')
    chat('저출산을 극복한 나라들은 어디가 있어?')
    print('두 번째 질문')
    chat('최신 관련 자료들의 문헌 제목을 알려줘')
