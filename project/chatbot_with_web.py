from langchain_text_splitters import RecursiveCharacterTextSplitter
from my_langchain.chains.llm_chain import LLMChain
from my_langchain.vectorstores import Chroma
from my_langchain.chat_models import ChatOpenAI
from my_langchain.document_loaders import WebBaseLoader

class ChatbotWithWeb:
    def __init__(self, url: str):
        self.llm = ChatOpenAI();
        
        loader = WebBaseLoader(url)
        pages = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=200)
        splits = text_splitter.split_text(pages)

        self.vectorestore = Chroma.from_texts(texts=splits)
        
    def __call__(self, query: str):
        doc = self.vectorestore.similarity_search(query)
        self.qa = LLMChain.from_llm(llm = self.llm, retriver=doc)
        print(self.qa(query))

def main():
    chat2 = ChatbotWithWeb(url = 'http://18children.president.pa.go.kr/mobile/our_space/fairy_tales.php?srh%5Bcategory%5D=07&srh%5Bview_mode%5D=detail&srh%5Bseq%5D=1204')
    chat2('삼형제의 재주는 각각 무엇인가요?')
    chat2('누구의 음식을 훔쳤나요?')

if __name__ == '__main__':
   main()
    