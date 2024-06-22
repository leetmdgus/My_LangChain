from my_langchain.schema import AIMessage, HumanMessage

class ConversationBufferMemory:
  history = []
  def __init__(self):
    self.history = []

  def add_history(self, userTxt, llmTxt):
    self.history.append(HumanMessage(userTxt).message)
    self.history.append(AIMessage(llmTxt).message)
    if len(self.history) > 10:
      self.history = self.history[2:]

  def get_history(self):
      return self.history
