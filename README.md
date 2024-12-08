# 🔗 My_LangChain

> LangChain 프레임워크를 자체 구현한 프로젝트입니다. 9개의 모듈과 4개의 프로젝트로 구성되어 있습니다.

## 📋 프로젝트 개요

- **진행 기간**: 2024/05/09 ~ 2024/06/23 (6주)
- **최종 수정일**: 2024/06/24
- **환경 설정**: OPENAI_API_KEY 환경변수 필요

## 🚀 구현된 프로젝트

### 1. 📚 ChatbotWithPDF
> PDF의 url을 입력하고, 그에 해당하는 질문을 하게 되면 pdf를 참고하여 응답을 생성하는 chatbot

```python
from my_langchain.chains.llm_chain import LLMChain
from my_langchain.text_splitter import RecursiveCharacterTextSplitter
from my_langchain.document_loaders import PyPDFLoader
from my_langchain.vectorstores import Chroma
from my_langchain.chat_models import ChatOpenAI

def main():
    chat = ChatbotWithPDF(pdf = "https://snuac.snu.ac.kr/2015_snuac/wp-content/uploads/2015/07/asiabrief_3-26.pdf")
    chat('저출산을 극복한 나라들은 어디가 있어?')
```

### 2. 🌐 ChatbotWithWeb
> web url을 입력하고, 그에 해당하는 질문을 하게 되면 web을 참고하여 응답을 생성하는 chatbot

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter
from my_langchain.chains.llm_chain import LLMChain
from my_langchain.vectorstores import Chroma
from my_langchain.chat_models import ChatOpenAI
from my_langchain.document_loaders import WebBaseLoader

def main():
    chat = ChatbotWithWeb(url = 'http://example.com')
    chat('질문 내용')
```

### 3. 💬 ConversationBot
> GUI를 통해 사용자와 상호작용을 할 수 있는 chatbot
> GUI는 ChatGPT를 통해 구현

```python
from my_langchain.chat_models import ChatOpenAI
from my_langchain.memory import ConversationBufferMemory
from my_langchain.chains import ConversationChain
```

### 4. 🔍 MyGoogleAgent
> 질문을 받으면 google에서 최신 자료를 찾아 그것을 url로 넘겨 받은 후, url을 langchain.webbaseLoader로 받은 후 RAG 방식으로 정보를 제공하는 프로그램

```python
from my_langchain.agents.tool import search_google
from my_langchain.document_loaders import WebBaseLoader
from my_langchain.text_splitter import RecursiveCharacterTextSplitter
from my_langchain.chat_models import ChatOpenAI
from my_langchain.vectorstores import Chroma
from my_langchain.chains import LLMChain
```

## 🔧 개선 예정 사항
- callbacks 모듈 구현
- agents 모듈 추가 구현
- OpenAI API 호출 최적화
