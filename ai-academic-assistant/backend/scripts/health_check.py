# scripts/health_check.py

from rag.services import health_service


def main():
    status = health_service.status()

    print("System Status:")
    print(f"Vector count: {status['vector_count']}")
    print(f"Status: {status['status']}")


if __name__ == "__main__":
    main()