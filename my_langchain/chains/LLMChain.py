# from langchain.chat_models import ChatOpenAI

# from langchain.prompts import (
#     ChatPromptTemplate,
#     MessagesPlaceholder,
#     SystemMessagePromptTemplate,
#     HumanMessagePromptTemplate,
# )

class History:
    def __init__(self):
        self.human
        self.ai
        
class LLMChain:
    def __init__(self, llm, prompt, verbos, memory):
        self.historys = []
        self.llm = llm;
        self.prompt = prompt
        self.verbos = verbos
        self.memory = memory
    def __call__(self, input:dict):
        print(input)

chain = LLMChain(1, 2, 3, 4)
chain({2, 3})
