from My_LangChain.my_langchain.chat_models import MyOpenAI

class ConversationSummaryMemory:
  def __init__(self, client:MyOpenAI):
    self.client = client
    self.user_history = ['','','']
    self.llm_history=['','','']
    
    self.user_chat_summary_history = ''
    self.llm_chat_summary_history = ''
    
    self.user_summary =''
    self.llm_summary=''


  def add_history(self, userTxt, llmTxt): 
    self._summary()
    self.user_history.append(userTxt)
    self.llm_history.append(llmTxt)
    self.user_history = self.user_history[1:]
    self.llm_history = self.llm_history[1:]
    
  #이부분 미숙. 요약 다시 해야함
  def _summary(self):
    self.user_chat_summary_history = self.user_summary+self.user_history[0]+self.user_history[1]+self.user_history[2]
    self.llm_chat_summary_history = self.llm_summary+self.llm_history[0]+self.llm_history[1]+self.llm_history[2]
    
    # self.user_summary = self.client.predict(self.user_chat_summary_history+'여태까지 했던 말들이야. 이를 요약해줘.')
    # self.llm_summary = self.client.predict(self.llm_chat_summary_history +'여태까지 했던 말들이야. 이를 요약해줘.')
    
  def get_history(self) -> tuple:
    return (self.user_chat_summary_history, self.llm_chat_summary_history)


if __name__ == '__main__':
  client = MyOpenAI()
  txt = '안녕 나는 한림대학교 소프트웨어학부 학생이야.'
  response = client.predict(txt)
  # print(txt)
  # print(response)
  
  memory = ConversationSummaryMemory(client)
  memory.add_history(txt, response)
  
  txt = '모두가 알다싶이 나는 사과를 좋아해'
  response = client.predict(txt)
  memory.add_history(txt, response)
  
  txt = '내가 좋아하는 과일이 뭐라고?'
  response = client.predict(txt)
  memory.add_history(txt, response)
  
  history = memory.get_history()
  print(history[0])
  print(history[1])
  
  
  