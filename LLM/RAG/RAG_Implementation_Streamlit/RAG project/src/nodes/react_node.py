from src.state.rag_state import State
from langchain_core.documents import Document
from langchain_core.tools import Tool
from langchain_core.messages import HumanMessage
from langchain.agents import create_agent
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun 

class Nodes:
    def __init__(self, retriever, llm):
        self.retriever = retriever
        self.llm = llm
        self._agent = None

    def retrieve_docs(self, state):
        docs = self.retriever.invoke(state.question)
        return State(
            question=state.question,
            retrieved_docs=docs
        )
    
    def build_tools(self):

        def retriever_tool_fn(query):
            docs = self.retriever.invoke(query)
            if not docs:
                return "No documents found."
            merged = []
            for i, doc in enumerate(docs[:8], start=1):
                metadata = doc.metadata if hasattr(doc, 'metadata') else {}
                title = metadata.get('title') or metadata.get('source') or f"doc_{i}"
                merged.append(f"[{i}] {title}\n{doc.page_content}")
            return "\n\n".join(merged)
        
        retriever_tool = Tool(
            name='retriever',
            description='Fetch passages from indexed vectorstore',
            func=retriever_tool_fn
        )

        wiki=WikipediaQueryRun(
            api_wrapper=WikipediaAPIWrapper(top_k_results=3, lang='en')
        )
        wikipedia_tool = Tool(
            name='wikipadia',
            description='Search Wikipedia for general knowledge.',
            func=wiki.run
        )

        return [retriever_tool, wikipedia_tool]


    def build_agent(self):
        tools = self.build_tools()
        prompt = (
            "You are a helpful RAG agent."
            "Prefer 'retriever' for user-provided docs; use 'wikipedia' for general knowledge."
            "Return only the final useful answer."
        )
        self._agent = create_agent(
            model=self.llm,
            system_prompt=prompt,
            tools=tools
        )

    def generate_answer(self, state):
        if self._agent is None:
            self.build_agent()
        
        response = self._agent.invoke({'messages':[HumanMessage(content=state.question)]})
        messages = response.get('messages', [])
        if messages:
            answer_msg = messages[-1]
            answer = getattr(answer_msg, 'content', None)

        return State(
            question=state.question,
            retrieved_docs=state.retrieved_docs,
            answer=answer or 'could not generate answer'
        )