# rag/ingestion/extractor.py

import fitz


class PDFExtractor:
    """
    Extracts page-wise text from PDF using PyMuPDF.
    Preserves page number for metadata.
    """

    def extract(self, file_path: str) -> list[dict]:
        pages = []

        try:
            doc = fitz.open(file_path)

            for page_index in range(len(doc)):
                page = doc[page_index]
                text = page.get_text()

                pages.append({
                    "page": page_index + 1,
                    "text": text
                })

            doc.close()
            return pages

        except Exception as e:
            raise RuntimeError(f"Failed to extract PDF: {file_path} | {str(e)}")