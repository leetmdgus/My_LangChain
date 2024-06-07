from My_LangChain.my_langchain.text_splitter import CharacterTextSplitter
from My_LangChain.my_langchain.document_loaders import PyPDFLoader

from My_LangChain.my_langchain.vectorstores import Chroma
from My_LangChain.my_langchain.chat_models import MyOpenAI
from My_LangChain.my_langchain.memory import ConversationSummaryMemory
from My_LangChain.my_langchain.chains import ConversationChain


class ChatbotWithPDF:
    def __init__(self, pdf: str):
        llm = MyOpenAI();
        
        loader = PyPDFLoader(pdf)
        pages = loader.load()

        text_splitter = CharacterTextSplitter(chunk_size=500)
        splits = text_splitter.split_text(pages)

        vectorestore = Chroma.from_texts(texts=splits)
        retriver = vectorestore.as_retriever()
        
        memory = ConversationSummaryMemory(llm)
        
        self.qa = ConversationChain.from_llm(llm = llm, memory=memory, retriver=retriver)
        # self.qa = ConversationChain.from_llm(llm = llm, memory=memory, retriver=None)
        
    def __call__(self, input: str):
        print(self.qa(input))


if __name__ == '__main__':
    loader = ChatbotWithPDF('https://snuac.snu.ac.kr/2015_snuac/wp-content/uploads/2015/07/asiabrief_3-26.pdf')
    print(loader("Tell me about the document"))
