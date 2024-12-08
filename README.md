# 🔗 My_LangChain

> LangChain 프레임워크를 자체적으로 구현한 프로젝트입니다.
> 9개의 모듈과, 그 모듈로 구현된 4개의 프로젝트가 있습니다.

## 📋 프로젝트 개요

- **진행 기간**: 6주 [2024/05/09~2024/06/23]
- **최종 수정일**: 2024/06/24
- **환경 설정**: OPENAI_API_KEY 환경변수 설정 필요

## 📝 개선 예정 사항
- callbacks 모듈 구현
- agents 모듈 추가 구현
- open_ai 호출 최적화

## 🚀 프로젝트 구성

### 1. ChatbotWithPDF
> pdf의 url을 입력하고, 그에 해당하는 질문을 하게 되면 pdf를 참고하여 응답을 생성하는 chatbot.

#### 사용법
```python
def main():
    chat = ChatbotWithPDF(pdf = "https://snuac.snu.ac.kr/2015_snuac/wp-content/uploads/2015/07/asiabrief_3-26.pdf")

    print('첫 번째 질문')
    chat('저출산을 극복한 나라들은 어디가 있어?')
    print('두 번째 질문')
    chat('최신 관련 자료들의 문헌 제목을 알려줘')
```

#### ChatbotWithPDF 클래스
```python
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
```

#### 필요 모듈
```python
from my_langchain.chains.llm_chain import LLMChain
from my_langchain.text_splitter import RecursiveCharacterTextSplitter
from my_langchain.document_loaders import PyPDFLoader
from my_langchain.vectorstores import Chroma
from my_langchain.chat_models import ChatOpenAI
```

### 2. ChatbotWithWeb
> web url을 입력하고, 그에 해당하는 질문을 하게 되면 web을 참고하여 응답을 생성하는 chatbot.

#### 사용법
```python
def main():
    chat2 = ChatbotWithWeb(url = 'http://18children.president.pa.go.kr/mobile/our_space/fairy_tales.php?srh%5Bcategory%5D=07&srh%5Bview_mode%5D=detail&srh%5Bseq%5D=1204')
    chat2('삼형제의 재주는 각각 무엇인가요?')
    chat2('누구의 음식을 훔쳤나요?') 
```

#### ChatbotWithWeb 클래스
```python
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
```

#### 필요 모듈
```python
from langchain_text_splitters import RecursiveCharacterTextSplitter
from my_langchain.chains.llm_chain import LLMChain
from my_langchain.vectorstores import Chroma
from my_langchain.chat_models import ChatOpenAI
from my_langchain.document_loaders import WebBaseLoader
```

### 3. ConversationBot
> GUI를 통해 사용자와 상호작용을 할 수 있는 chatbot입니다.
> GUI는 챗GPT를 통해 구현했습니다.

#### 사용법
```python
def main():
    #보기에 심심해 보여서 chat gpt를 통해 gui로 변경
    import tkinter as tk
    bot = ConversationBot()

    def send_message(event=None):
        user_message = entry_field.get()
        if user_message.strip() == '':
            return
        chat_log.config(state=tk.NORMAL)
        chat_log.insert(tk.END, "You: " + user_message + "\n\n")
        chat_log.config(state=tk.DISABLED)
        entry_field.delete(0, tk.END)
        receive_message(f"{bot.conversation(user_message)}.")

    def receive_message(response):
        chat_log.config(state=tk.NORMAL)
        chat_log.insert(tk.END, "Bot: " + response + "\n\n")
        chat_log.config(state=tk.DISABLED)

    # GUI 창 생성
    root = tk.Tk()
    root.title("Chatbot")

    # 대화 내용 표시할 곳
    chat_log = tk.Text(root, bd=0, height=8, width=50, font="Arial")
    chat_log.config(state=tk.DISABLED)

    scrollbar = tk.Scrollbar(root, command=chat_log.yview, cursor="heart")
    chat_log['yscrollcommand'] = scrollbar.set

    # 입력 필드
    entry_field = tk.Entry(root, bg="white", width=50)
    entry_field.bind("<Return>", send_message)

    # 전송 버튼
    send_button = tk.Button(root, text="Send", command=send_message)

    # 배치
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    chat_log.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    entry_field.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    send_button.pack(side=tk.RIGHT)

    # GUI 시작
    root.mainloop()
```

#### ConversationBot 클래스
```python
class ConversationBot:
    def __init__(self):
        llm = ChatOpenAI()
        memory = ConversationBufferMemory()
        self.chain = ConversationChain.from_llm(llm=llm, memory=memory, retriver=None)
    
    def conversation(self, txt):
        return self.chain(txt)
```

#### 필요 모듈
```python
from my_langchain.chat_models import ChatOpenAI
from my_langchain.memory import ConversationBufferMemory
from my_langchain.chains import ConversationChain
```

### 4. MyGoogleAgent
> 질문을 받으면 google에서 최신 자료를 찾아 그것을 url로 넘겨 받은 후
> url을 langchain.webbaseLoader로 받은 후
> RAG 방식으로 정보를 제공하는 프로그램

#### 사용법
```python
def main():
    # 1. Get user's question in English
    user_query = input("Enter your question in English: ")

    # 2. Search Google with the user's question
    google_query = make_query(user_query)
    urls = search_google(google_query)

    # 3. Provide answer using RAG approach with the returned URL
    play_rag(user_query, urls)
```

#### play_rag함수와 make_query함수
```python
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
```

#### 필요 모듈
```python
from my_langchain.agents.tool import search_google
from my_langchain.document_loaders import WebBaseLoader
from my_langchain.text_splitter import RecursiveCharacterTextSplitter
from my_langchain.chat_models import ChatOpenAI
from my_langchain.vectorstores import Chroma
from my_langchain.chains import LLMChain
```
