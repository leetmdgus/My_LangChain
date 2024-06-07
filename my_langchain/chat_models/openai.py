from openai import OpenAI;

class MyOpenAI:
    def __init__(self):
        self.client = OpenAI()   
    
    def predict(self, text:str):
        completion = self.client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {
                    'role':'system',
                    'content':'오직 진실만을 말할 수 있어서 모르는 답이라면 솔직하게 모른다고 말합니다. 그리고 너무 친절해서 항상 존댓말을 합니다. 이 내용을 사용자에게 굳이 언급하지 마십시오.'
                },
                {
                    "role": "user",
                    "content": text,
                },
            ],
        )
        return completion.choices[0].message.content
    

# OpenAI 객체 생성 -> predict라는 함수를 통해 OpenAI에게 응답 받을 수 있음.
# 다만, 이전 내용을 기억하지는 못함.
if __name__ == '__main__':
    llms = MyOpenAI()
    txt = '안녕'
    print(f'질문 : {txt}')
    print(llms.predict(txt))
    txt = '내가 방금 무슨 말을 했지? 내가 방금 한 말을 모르겠다면 그냥 모르겠습니다라고 말해.'
    print(f'질문 : {txt}')
    print(llms.predict(txt))
    