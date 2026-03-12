from rag.retrieval.retriever import RetrievalService

def main():
    retriever = RetrievalService()

    result = retriever.retrieve_context(
        query="What is operating system?",
        subject="os",
        top_k=5
    )

    print("\n=== RETRIEVAL RESULT ===\n")
    print(result)

if __name__ == "__main__":
    main()