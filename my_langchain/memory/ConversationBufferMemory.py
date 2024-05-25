class ConversationBufferMemoryClass:
    def __init__(self, memory_key, return_messages):
        self.memory_key = memory_key
        self.return_messages = return_messages
        self.chat_history = []

    def add_message(self, message:str):
        self.chat_history.append(message)

    def get_memory(self):
        return self.chat_history if self.return_messages else []