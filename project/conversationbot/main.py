from .conversationbot import ConversationBot


bot = ConversationBot()
print('안녕하십니까 사용자와 상호작용하는 대화형 인공지능입니다. 만약 대화를 끝내고 싶으시다면 -1을 입력하세요.')

while True:
    txt = input('당신: ')
    if(txt == '-1'): 
        break
    
    print(f'챗봇: {bot.conversation(txt)}')

    