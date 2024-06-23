# https://teddylee777.github.io/langchain/langchain-agent/

import os

# TAVILY API KEY를 기입합니다.
os.environ["TAVILY_API_KEY"] = "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"

# TavilySearchResults 클래스를 langchain_community.tools.tavily_search 모듈에서 가져옵니다.
from langchain_community.tools.tavily_search import TavilySearchResults

# TavilySearchResults 클래스의 인스턴스를 생성합니다
# k=5은 검색 결과를 5개까지 가져오겠다는 의미입니다
search = TavilySearchResults(k=5)

# 검색 결과를 가져옵니다.
res = search.invoke("판교 카카오 프렌즈샵 아지트점의 전화번호는 무엇인가요?")
print(res[0]['content'])