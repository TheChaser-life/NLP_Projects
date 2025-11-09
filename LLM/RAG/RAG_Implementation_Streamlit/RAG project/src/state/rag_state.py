from typing import List
from pydantic import BaseModel
from langchain_core.documents import Document

class State(BaseModel):
    question:str
    retrieved_docs:List[Document] = []
    answer:str = ""