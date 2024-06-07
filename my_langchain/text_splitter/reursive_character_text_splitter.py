# # chunk size =  chunk의 최대 크기
# # chunk_overlap= chunk의 겹치는 갯수 
# class RecursiveCharacterTextSplitterClass:
#     def __init__(self, chunk_size=1000, chunk_overlap=100):
#         self.chunk_size = chunk_size
#         self.chunk_overlap = chunk_overlap
#         self.separators = ['\n\n', '\n', '.']

#     def create_documents(self, text: str):
#         return self._split_text(text, 0)

#     def _split_text(self, text, separators_idx=0):
#         if separators_idx >= len(self.separators):
#             return self._split_by_chunk_size(text)

#         separator = self.separators[separators_idx]
#         parts = text.split(separator)

#         if len(parts) == 1:
#             return self._split_text(text, separators_idx + 1)

#         chunks = []
#         buffer = ""

#         for part in parts:
#             if len(buffer + separator + part) <= self.chunk_size:
#                 buffer += (separator if buffer else "") + part
#             else:
#                 if buffer:
#                     chunks.append(buffer)
#                 buffer = part

#         if buffer:
#             chunks.append(buffer)

#         split_chunks = []
#         for chunk in chunks:
#             split_chunks.extend(self._split_text(chunk, separators_idx + 1))

#         return self._combine_chunks(split_chunks)

#     def _split_by_chunk_size(self, text: str):
#         chunks = []
#         start = 0 if text[0] != ' ' else 1
        
#         while start < len(text):
#             end = start + self.chunk_size
#             chunk = text[start:end]
#             chunks.append(chunk)
#             start += self.chunk_size - self.chunk_overlap
#         return chunks

#     def _combine_chunks(self, chunks):
#         if not chunks:
#             return []
        
#         combined_chunks = [chunks[0]]
#         for i in range(1, len(chunks)):
#             if len(combined_chunks[-1]) + len(chunks[i]) - self.chunk_overlap <= self.chunk_size:
#                 combined_chunks[-1] += chunks[i][self.chunk_overlap:]
#             else:
#                 combined_chunks.append(chunks[i])
        
#         return combined_chunks

# # 예제 사용
# if __name__ == '__main__':
#     text = "This is a long text. It contains multiple sentences and paragraphs.\n\nWe want to split it into chunks."
#     print(text)
#     print("================")
#     splitter = RecursiveCharacterTextSplitterClass(chunk_size=50, chunk_overlap=10)
#     chunks = splitter.create_documents(text)

#     for chunk in chunks:
#         print(chunk)
