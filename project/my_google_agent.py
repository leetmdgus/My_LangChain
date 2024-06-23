# 질문을 받으면, 
# google에서 최신 자료를 찾아. 
# 그것을 url로 넘겨 받은 후 
# url을 langchain.webbaseLoader로 받은 후
# rag방식으로 정보를 제공하는 프로그램

from my_langchain.agents.tool import search_google
from my_langchain.document_loaders import WebBaseLoader
from my_langchain.text_splitter import RecursiveCharacterTextSplitter
from my_langchain.chat_models import ChatOpenAI
from my_langchain.vectorstores import Chroma
from my_langchain.chains import LLMChain

def play_rag(query, urls):
    llm = ChatOpenAI()

    for url in urls:
        loader = WebBaseLoader(url)
        text = loader.load()

        if text == ' ':
            continue

        splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=0)
        text_chunks = splitter.split_text(text)
        
        db = Chroma.from_texts(text_chunks)
        retriever = db.similarity_search(query)

        if retriever == [' ']:
            continue
    
        chain = LLMChain(llm, retriever=retriever)
        response = chain(query)
        print(response)
        return response
    
    print('죄송합니다. 정보를 찾을 수 없습니다.')

def make_query(query):
    llm = ChatOpenAI()
    return llm.predict(f'to aquire the resopnse about "{query}", make the a proper question, and just only say that in English.')

def main():
    # 1. Get user's question in English
    user_query = input("Enter your question in English: ")

    # 2. Search Google with the user's question
    google_query = make_query(user_query)
    urls = search_google(google_query)

    # 3. Provide answer using RAG approach with the returned URL
    play_rag(user_query, urls)

#개선해야할 점: 응답 속도가 매우 느림
if __name__ == "__main__":
    # 질문 예시 
    # 1. What time is it? 
    # 2. Tell me about the tomorrow's weather
    # 3. Tell me about the korean food restaurant in Seoul
    # 4. Tell me about the langchain
    # 5. How was the insideout2?
    # 6. Are there currently news articles that I have to noticed?

    main()