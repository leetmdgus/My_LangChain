# pip install langchain openai tiktoken chromadb pypdf langchain_community langchain-openai

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.memory import ConversationBufferMemory


from langchain_community.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain


from My_LangChain.my_langchain.openai_api_key import OPENAI_KEY
OPENAI_API_KEY = OPENAI_KEY().OPENAI_API_KEY;

class ChatbotWithPDF:
    def __init__(self, pdf:str):
        # url을 통해서 pdf 정보 가져오기
        loader = PyPDFLoader(pdf)
        pages = loader.load_and_split()

        # # PDF 내용을 작은 chunk 단위로 나누기
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
        splits = text_splitter.split_documents(pages)

        #OpenAI Embedding 모델을 이용해서 Chunk를 Embedding한 후 Vector Store에 저장
        vectorestore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY))
        memory = ConversationBufferMemory(
            memory_key = 'chat_history', return_messages=True
        )

        llm = ChatOpenAI(openai_api_key = OPENAI_API_KEY)
        retriever = vectorestore.as_retriever()

        self.qa = ConversationalRetrievalChain.from_llm(llm, retriever=retriever, memory=memory)
        
    def __call__(self, input:str):
        print(self.qa(input))
