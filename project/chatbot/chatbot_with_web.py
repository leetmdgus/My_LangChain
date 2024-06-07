from My_LangChain.my_langchain.text_splitter import CharacterTextSplitter

from My_LangChain.my_langchain.vectorstores import Chroma
from My_LangChain.my_langchain.chat_models import MyOpenAI
from My_LangChain.my_langchain.memory import ConversationSummaryMemory
from My_LangChain.my_langchain.chains import ConversationChain

from My_LangChain.my_langchain.openai_api_key import OPENAI_KEY
OPENAI_API_KEY = OPENAI_KEY().OPENAI_API_KEY

from My_LangChain.my_langchain.document_loaders import WebBaseLoader

class ChatbotWithWeb:
    def __init__(self, url: str):
        llm = MyOpenAI();
        
        loader = WebBaseLoader(url)
        pages = loader.load()

        text_splitter = CharacterTextSplitter(chunk_size=500)
        splits = text_splitter.split_text(pages)

        vectorestore = Chroma.from_texts(texts=splits)
        retriver = vectorestore.as_retriever()
        
        memory = ConversationSummaryMemory(llm)
        
        self.qa = ConversationChain.from_llm(llm = llm, memory=memory, retriver=retriver)
        
    def __call__(self, input: str):
        return self.qa(input)

if __name__ == '__main__':
    chat2 = ChatbotWithWeb(url = 'http://18children.president.pa.go.kr/mobile/our_space/fairy_tales.php?srh%5Bcategory%5D=07&srh%5Bview_mode%5D=detail&srh%5Bseq%5D=1204')
    # print(loader.load_and_split()) 
    # print(len(loader.load_and_split()))
    print(chat2('삼형재의 재주는 각각 무엇인가요?'))
    print(chat2('누구의 음식을 훔쳤나요?'))
    