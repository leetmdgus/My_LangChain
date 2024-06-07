import requests
from bs4 import BeautifulSoup

class WebBaseLoader:
    def __init__(self, url: str):
        self.url = url
        
        # 웹 페이지 다운로드
        response = requests.get(self.url)
        if response.status_code == 200:
            self.html_content = response.content
        else:
            raise Exception(f"Failed to download web page: status code {response.status_code}")

    # string 값 반환
    def load(self):
        soup = BeautifulSoup(self.html_content, 'html.parser')
        text = soup.get_text(separator=' ')
        return text.strip()
    
    # List<string> 값 반환
    def load_and_split(self):
        soup = BeautifulSoup(self.html_content, 'html.parser')
        elements = soup.find_all(['p', 'div', 'span', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        texts = [element.get_text(separator=' ').strip() for element in elements if element.get_text(strip=True)]
        return texts

if __name__ == '__main__':
    loader = WebBaseLoader('https://n.news.naver.com/article/214/0001350812?cds=news_media_pc&type=editn')
    # loader = WebBaseLoader('http://18children.president.pa.go.kr/mobile/our_space/fairy_tales.php?srh%5Bcategory%5D=07&srh%5Bview_mode%5D=detail&srh%5Bseq%5D=1204')
    print(loader.load())