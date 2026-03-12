# scripts/test_retrieval.py

from rag.services import generate_answer
from rag.config import validate_config


def main():
    validate_config()

    query = input("Enter question: ")
    subject = input("Enter subject: ")

    response = generate_answer(query, subject)

    print("\nANSWER:\n")
    print(response["answer"])

    print("\nSources:")
    for chunk in response["retrieved_chunks"]:
        print(f"{chunk['source']} (Page {chunk['page']})")


if __name__ == "__main__":
    main()