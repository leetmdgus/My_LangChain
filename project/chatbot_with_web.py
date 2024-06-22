from my_langchain.text_splitter import CharacterTextSplitter

from my_langchain.vectorstores import Chroma
from my_langchain.chat_models import ChatOpenAI
from my_langchain.memory import ConversationSummaryMemory
from my_langchain.chains import ConversationChain


from my_langchain.document_loaders import WebBaseLoader

class ChatbotWithWeb:
    def __init__(self, url: str):
        llm = ChatOpenAI();
        
        loader = WebBaseLoader(url)
        pages = loader.load()

        text_splitter = CharacterTextSplitter(chunk_size=500)
        splits = text_splitter.split_text(pages)

        vectorestore = Chroma.from_texts(texts=splits)
        retriver = vectorestore.as_retriever()
        
        memory = ConversationSummaryMemory(llm)
        
        self.qa = ConversationChain.from_llm(llm = llm, memory=memory, retriver=retriver)
        
    def __call__(self, input: str):
        print(self.qa(input))

if __name__ == '__main__':
    chat2 = ChatbotWithWeb(url = 'http://18children.president.pa.go.kr/mobile/our_space/fairy_tales.php?srh%5Bcategory%5D=07&srh%5Bview_mode%5D=detail&srh%5Bseq%5D=1204')
    chat2('삼형제의 재주는 각각 무엇인가요?')
    chat2('누구의 음식을 훔쳤나요?')

    