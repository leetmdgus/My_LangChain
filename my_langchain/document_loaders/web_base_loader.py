import requests
from bs4 import BeautifulSoup

class WebBaseLoader:
    def __init__(self, url: str):
        self.url = url
        self.text_content = ""

    def load(self):
        # HTTP GET 요청 보내기
        response = requests.get(self.url)
        
        # 응답이 성공적인지 확인
        if response.status_code == 200:
            # BeautifulSoup을 사용하여 HTML 파싱
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 모든 텍스트 내용 추출
            self.text_content = soup.get_text(separator=' ', strip=True)
        else:
            print(f"Failed to retrieve content from {self.url}. Status code: {response.status_code}")

        return self.text_content
