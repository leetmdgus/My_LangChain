import chromadb

class Chroma:
    def __init__(self, texts):
        self.texts = texts
        self.chroma_client = chromadb.Client()
        self.collection = self.chroma_client.get_or_create_collection(name="sample_collection")
        self.collection.upsert(
            documents=self.texts,
            ids=[str(i) for i in range(len(self.texts))] 
        )

    @classmethod
    def from_texts(cls, texts):
        return cls(texts)
    
    #데이터 베이스에서 유사도가 높은 문서를 가져옴
    def similarity_search(self, query:str):
        results = self.collection.query(
            query_texts=[query], # Chroma will embed this for you
            n_results=len(self.texts) # how many results to return
        )
        
        return results['documents'][0]
