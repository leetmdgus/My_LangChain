from my_langchain.schema import AIMessage, HumanMessage

class ConversationBufferMemory:
  history = []
  def __init__(self, buffer_size = 10):
    self.history = []
    self.buffer_size = buffer_size

  def add_history(self, userTxt, llmTxt):
    self.history.append(HumanMessage(userTxt).message)
    self.history.append(AIMessage(llmTxt).message)
    if len(self.history) > self.buffer_size:
      self.history = self.history[2:]

  def get_history(self):
      return self.history
