from typing import List, Union
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_community.document_loaders import (
    WebBaseLoader,
    PyPDFLoader,
    TextLoader,
    PyPDFDirectoryLoader
)

class DocumentProcessor:
    """Handle document loading and processing"""

    def __init__(self, chunk_size:int=500, chunk_overlap:int=50):
        self.splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

    def load_from_url(self, url:str)->List[Document]:
        docs = WebBaseLoader(url).load()
        return docs 
    
    def load_from_pdf_dir(self, directory:Union[str, Path])->List[Document]:
        docs = PyPDFDirectoryLoader(str(directory)).load()
        return docs
    
    def load_from_txt(self, file_path:Union[str, Path])->List[Document]:
        docs = TextLoader(str(file_path), encoding='utf-8').load()
        return docs
    
    def load_from_pdf(self, file_path:Union[str, Path])->List[Document]:
        docs = PyPDFDirectoryLoader(str('data')).load()
        return docs
    
    def load_documents(self, sources):  
        docs = []

        for src in sources:

            if src.startswith("http://") or src.startswith("https://"):
                docs.extend(self.load_from_url(src))
    
            path = Path('data')
            if path.is_dir():
                docs.extend(self.load_from_pdf_dir(path))
            elif path.suffix.lower() == '.txt':
                docs.extend(self.load_from_txt(path))
        
        return docs
    
    def split_docs(self, docs):
        return self.splitter.split_documents(docs)
    
    def process_urls(self, urls):
        docs = self.load_documents(urls)
        return self.split_docs(docs)