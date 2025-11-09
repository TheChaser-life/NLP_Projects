from langgraph.graph import StateGraph, END
from src.state.rag_state import State
from src.nodes.react_node import Nodes

class GraphBuilder:

    def __init__(self, retriever, llm):
        self.nodes = Nodes(retriever=retriever, llm=llm)
        self.graph = None
        
    def build(self):
        builder = StateGraph(State)

        builder.add_node("retriever", self.nodes.retrieve_docs)
        builder.add_node('responder', self.nodes.generate_answer)

        builder.set_entry_point('retriever')
        builder.add_edge('retriever', 'responder')
        builder.add_edge('responder', END)
        
        self.graph = builder.compile()
        return self.graph
    
    def run(self, question):
        if self.graph is None:
            self.build()
        state = State(question=question)
        return self.graph.invoke(state)