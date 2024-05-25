from My_LangChain.my_langchain.document_loaders.PyPDFLoader import PyPDFLoaderClass
from My_LangChain.my_langchain.text_splitter.ReursiveCharacterTextSplitter import RecursiveCharacterTextSplitterClass

from My_LangChain.my_langchain.vectorstores.Chroma import ChromaClass
from My_LangChain.my_langchain.embedding.OpenAIEmbeddings import OpenAIEmbeddingsClass
from My_LangChain.my_langchain.memory.ConversationBufferMemory import ConversationBufferMemoryClass

from My_LangChain.my_langchain.chat_models.ChatOpenAI import ChatOpenAIClass
from My_LangChain.my_langchain.chains.ConversationalRetrievalChain import ConversationalRetrievalChainClass

from My_LangChain.my_langchain.openai_api_key import OPENAI_KEY
OPENAI_API_KEY = OPENAI_KEY().OPENAI_API_KEY

class ChatbotWithPDF:
    def __init__(self, pdf: str):
        loader = PyPDFLoaderClass(pdf)
        pages = loader.load_and_split()

        text_splitter = RecursiveCharacterTextSplitterClass(chunk_size=500, chunk_overlap=0)
        splits = text_splitter.split_documents(pages)

        vectorestore = ChromaClass.from_documents(documents=splits, embedding=OpenAIEmbeddingsClass(openai_api_key=OPENAI_API_KEY))
        memory = ConversationBufferMemoryClass(memory_key='chat_history', return_messages=True)

        llm = ChatOpenAIClass(openai_api_key=OPENAI_API_KEY)
        retriever = vectorestore.as_retriever()

        self.qa = ConversationalRetrievalChainClass.from_llm(llm, retriever=retriever, memory=memory)
        
    def __call__(self, input: str):
        print(self.qa(input))

if __name__ == '__main__':
    loader = ChatbotWithPDF('https://snuac.snu.ac.kr/2015_snuac/wp-content/uploads/2015/07/asiabrief_3-26.pdf')
    print(loader("Tell me about the document"))
