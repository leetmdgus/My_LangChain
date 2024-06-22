
class Chroma:
    def __init__(self, texts, embedding_funcion):
        self.texts = texts
        self.embedding_funcion = embedding_funcion #

    @classmethod
    def from_texts(cls, texts):
        return cls(texts)
    
    def as_retriever(self):

        return 
    
    #데이터 베이스에서 유사도가 높은 문서를 가져옴
    def similarity_search(self, query:str):
        #클라이언트 연결
        import chromadb
        client = chromadb.PersistentClient()

        #컬렉션 생성
        answers = client.create_collection(
            name="answers"
        )   

        #모델 불러오기
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer('snunlp/KR-SBERT-V40K-klueNLI-augSTS')
  
        #데이터 삽입하기
        ids = []
        metadatas = []
        embeddings = []

        for idx, text in enumerate(self.texts):            
            metadata = {
                'index':idx
            }
            
            embedding = model.encode(text, normalize_embeddings=True)
            
            ids.append(idx)
            metadatas.append(metadata)
            embeddings.append(embedding)
            
        chunk_size = 1024  # 한 번에 처리할 chunk 크기 설정
        total_chunks = len(embeddings) // chunk_size + 1  # 전체 데이터를 chunk 단위로 나눈 횟수

        for chunk_idx in range(total_chunks):
            start_idx = chunk_idx * chunk_size
            end_idx = (chunk_idx + 1) * chunk_size
            
            # chunk 단위로 데이터 자르기
            chunk_embeddings = embeddings[start_idx:end_idx]
            chunk_ids = ids[start_idx:end_idx]
            chunk_metadatas = metadatas[start_idx:end_idx]
            
            # chunk를 answers에 추가
            answers.add(embeddings=chunk_embeddings, ids=chunk_ids, metadatas=chunk_metadatas)
        
        #검색
        result = answers.query(
            query_embeddings=model.encode("삼형제의 재주는 각각 무엇인가요?", normalize_embeddings=True).tolist(),
            n_results=3
        )

        print(result)


