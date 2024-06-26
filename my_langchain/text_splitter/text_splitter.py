class CharacterTextSplitter:
    def __init__(self, separator:str = '\n', chunk_size:int = 500):
        self.separator = separator;
        self.chunk_size = chunk_size;
        
    def split_text(self, text:str):
        #seperator 기준으로 나누기
        chunks = []
        
        while True:
            if not '\n\n' in text:
                break
            text = text.replace('\n\n','')
        
        start = 0
        for index in range(len(text)):
            if(text[index] == self.separator):
                chunks.append(text[start:index])             
                start = index+1;
        chunks.append(text[start:])         
            
        # chunks_size로 나누기
        result = []
        for index in range(len(chunks)):    
            if(len(chunks[index]) <= self.chunk_size):
                result.append(chunks[index])
            else:
                start = 0; 
                while True:
                    if start >= len(chunks[index]):
                        break
                    result.append(chunks[index][start:start+self.chunk_size])
                    start += self.chunk_size
        return result
    
