class RecursiveCharacterTextSplitterClass:
    def __init__(self, chunk_size=500, chunk_overlap=0):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split_documents(self, documents):
        chunks = []
        for document in documents:
            start = 0
            while start < len(document):
                end = min(start + self.chunk_size, len(document))
                chunks.append(document[start:end])
                start += self.chunk_size - self.chunk_overlap
        return chunks