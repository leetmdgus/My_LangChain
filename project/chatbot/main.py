from My_LangChain.project.chatbot.My_Chatbot import ChatbotWithPDF

chat = ChatbotWithPDF(pdf = "https://snuac.snu.ac.kr/2015_snuac/wp-content/uploads/2015/07/asiabrief_3-26.pdf")

print('첫 번째 질문')
chat('저출산을 극복한 나라들은 어디가 있어?')
print('두 번째 질문')
chat('최신 관련 자료들의 문헌 제목을 알려줘')