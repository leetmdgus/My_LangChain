import requests
from pypdf import PdfReader

class PyPDFLoader:
    def __init__(self, pdf:str):
        # PDF 파일 URL
        url = pdf

        # 다운로드할 파일 경로 지정
        self.file_path = "./My_LangChain/downloads/downloaded_example.pdf"

        # PDF 파일 다운로드
        response = requests.get(url)
        if response.status_code == 200:
            with open(self.file_path, 'wb') as f:
                f.write(response.content)
        else:
            raise Exception(f"Failed to download file: status code {response.status_code}")
        
    #string 값 반환
    def load(self):
        reader = PdfReader(self.file_path)
        
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text
    
    # List<string>값 반환
    def load_and_split(self):
        # PDF 파일 읽기
        reader = PdfReader(self.file_path)
        texts = [page.extract_text() for page in reader.pages]
        return texts        
    