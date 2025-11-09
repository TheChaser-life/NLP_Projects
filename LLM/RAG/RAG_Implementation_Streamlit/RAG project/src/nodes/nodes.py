from src.state.rag_state import State

class Nodes:
    def __init__(self, retriever, llm):
        self.retriever = retriever
        self.llm = llm

    def retrieve_docs(self, state):
        docs = self.retriever.invoke(state.question)
        return State(
            question=state.question,
            retrieved_docs=docs
        )
    
    def generate_answer(self, state):
        context = '\n\n'.join([doc.page_content for doc in state.retrieved_docs])

        prompt = f"""Answer the question based on the context.
            
            Context:
            {context}

            Question: {state.question}
        """

        response = self.llm.invoke(prompt)
        return State(
            question=state.question,
            retrieved_docs=state.retrieved_docs,
            answer=response.content
        )