# # chunk size =  chunk의 최대 크기
# # chunk_overlap= chunk의 겹치는 갯수 
class RecursiveCharacterTextSplitter:
    def __init__(self, chunk_size = 300, chunk_overlap = 100):
        self.chunk_size:int = chunk_size
        self.chunk_overlap:int = chunk_overlap

    def split_text(self, text:str):
        # 단어 단위로 text split

        text = text.replace('\n', ' ')
        text = text.replace('.', ' ')
        text = text.replace(',', ' ')
        text = text.replace('\t', ' ')
        while '  ' in text:
            text = text.replace('  ', ' ')

        chunks = text.split(' ')


        #chunk_size - chunk_overlap 사이즈로 분할하기
        splited_chunk = []
        for chunk in chunks:
            if len(chunk) > self.chunk_size - self.chunk_overlap:
                splited_chunk.append(chunk[0:len(chunk)//2])
                splited_chunk.append(chunk[len(chunk)//2:])
            else:
                splited_chunk.append(chunk)
                

        #chunk_overlap만큼 앞에 반복하고 chunk_size - chunk_overlap만큼 합치기
        new_chunk = []
        word = ''
        base = -1
        for idx, chunk in enumerate(splited_chunk):
            if len(word + chunk) <= self.chunk_size - self.chunk_overlap:
                word += chunk + ' '
            else:
                for j in range(base-1, -1, -1):
                    if len(word + splited_chunk[j]) < self.chunk_size:
                        word = f'{splited_chunk[j]} {word}'
                    else:
                        break
                base = idx

                new_chunk.append(word)
                word = chunk + ' '

        for j in range(base-1, -1, -1):
            if len(word + splited_chunk[j]) < self.chunk_size:
                word = f'{splited_chunk[j]} {word}'
            else:
                break
        new_chunk.append(word)
        return new_chunk

