from my_langchain.chat_models import ChatOpenAI
from my_langchain.memory import ConversationBufferMemory
from my_langchain.chains import ConversationChain

class ConversationBot:
    def __init__(self):
        llm = ChatOpenAI()
        memory = ConversationBufferMemory()
        self.chain = ConversationChain.from_llm(llm=llm, memory=memory, retriver=None)
    
    def conversation(self, txt):
        return self.chain(txt)
    

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

if __name__ == '__main__':
    main()