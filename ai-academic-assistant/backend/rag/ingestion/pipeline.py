# rag/ingestion/pipeline.py

import os
from pathlib import Path
from time import time

from rag.ingestion.extractor import PDFExtractor
from rag.ingestion.cleaner import TextCleaner
from rag.ingestion.document_hash import compute_file_hash
from rag.ingestion.registry import DocumentRegistry

from rag.chunking.token_chunker import TokenChunker
from rag.embeddings.model import EmbeddingModel
from rag.vector_store.manager import VectorIndex

from rag.config import DATA_DIR, DOC_REGISTRY_PATH


class IngestionPipeline:
    """
    Production-safe ingestion pipeline.
    """

    def __init__(self):
        self.extractor = PDFExtractor()
        self.cleaner = TextCleaner()
        self.chunker = TokenChunker()
        self.embedder = EmbeddingModel()
        self.vector_index = VectorIndex()
        self.registry = DocumentRegistry(DOC_REGISTRY_PATH)

    # --------------------------------------------------

    def ingest_single_document(self, file_path: str, subject: str):
        start_time = time()

        file_hash = compute_file_hash(file_path)

        if self.registry.exists(file_hash):
            print(f"Skipping already indexed file: {file_path}")
            return

        pages = self.extractor.extract(file_path)

        all_chunks = []

        for page in pages:
            cleaned_text = self.cleaner.clean(page["text"])

            if not cleaned_text:
                continue

            base_metadata = {
                "subject": subject.lower(),
                "source": os.path.basename(file_path),
                "page": page["page"]
            }

            chunks = self.chunker.chunk(cleaned_text, base_metadata)

            for chunk in chunks:
                # CRITICAL FIX: store text inside metadata
                all_chunks.append({
    "text": chunk["text"],
    "metadata": {
        **chunk["metadata"],
        "chunk_id": f"{os.path.basename(file_path)}_{page['page']}_{len(all_chunks)}",
        "text": chunk["text"]
    }
})

        if not all_chunks:
            print(f"No valid chunks found in {file_path}")
            return

        texts = [c["text"] for c in all_chunks]
        metadatas = [c["metadata"] for c in all_chunks]

        embeddings = self.embedder.embed(texts)

        self.vector_index.add(embeddings, metadatas)

        self.registry.add(file_hash)

        elapsed = round(time() - start_time, 2)
        print(f"Ingested {file_path} in {elapsed}s")

    # --------------------------------------------------

    def ingest_all_documents(self):
        for subject_dir in Path(DATA_DIR).iterdir():
            if not subject_dir.is_dir():
                continue

            subject = subject_dir.name.lower()

            for file in subject_dir.glob("*.pdf"):
                self.ingest_single_document(str(file), subject)