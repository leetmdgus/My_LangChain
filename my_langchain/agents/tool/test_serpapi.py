# 구글이나 야후 검색을 API로 하는 SerpApi라는 웹 서비스와 연동할 수 있다. 
# 언어 모델이 알지 못하는 정보를 구글 등에서 가져오는데 사용된다. 

# serpApi api 를 받아와야한다.

# pip install google-search-results
# https://serpapi.com

from langchain.agents import AgentType, initialize_agent, load_tools
from langchain_openai import OpenAI

if __name__ == "__main__":
    llm = OpenAI(temperature=0)
    tools = load_tools(["serpapi", "llm-math"], llm=llm)
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    agent.run("오늘 대한민국 가장 높은 기온이 몇도야?")