
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


class WebBaseLoader:
    def __init__(self, url: str):
        # 웹드라이버 설정
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # 브라우저를 띄우지 않고 실행
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        # 웹드라이버 실행
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

        # 웹 페이지 열기
        driver.get(url)

        # 페이지의 전체 HTML 소스를 문자열로 가져오기
        page_source = driver.page_source

        # 웹드라이버 종료
        driver.quit()

        # BeautifulSoup으로 HTML 파싱
        soup = BeautifulSoup(page_source, 'html.parser')

        # 모든 텍스트 내용 추출
        self.text_content = soup.get_text(separator=' ', strip=True)
                
    # string 값 반환
    def load(self):
        return self.text_content
    

if __name__ =='__main__':
    loader = WebBaseLoader('https://www.tripadvisor.com/Restaurants-g294197-c10661-Seoul.html')
    print(loader.load())