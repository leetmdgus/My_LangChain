from chromadb import ChromaDB

from My_LangChain.my_langchain.embedding.OpenAIEmbeddings import OpenAIEmbeddingsClass

class ChromaClass:
    def __init__(self):
        self.chroma_db = ChromaDB()
        self.documents = []
        self.embeddings = []

    @classmethod
    def from_documents(cls, documents, embedding: OpenAIEmbeddingsClass):
        instance = cls()
        instance.documents = documents
        instance.embeddings = [embedding.embed(doc) for doc in documents]
        instance.index_documents()
        return instance

    def index_documents(self):
        for doc, emb in zip(self.documents, self.embeddings):
            self.chroma_db.index_document(doc, emb)

    def as_retriever(self):
        return self

    def retrieve(self, query_embedding):
        return self.chroma_db.search(query_embedding)
