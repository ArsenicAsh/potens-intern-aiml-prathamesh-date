from pathlib import Path


def load_documents(doc_folder="docs"):
    """
    Load all Markdown documents from the knowledge base.

    Returns:
        List of dictionaries:
        {
            "filename": "...",
            "content": "..."
        }
    """

    documents = []

    folder = Path(doc_folder)

    if not folder.exists():
        raise FileNotFoundError(f"Document folder '{doc_folder}' not found.")

    for file in sorted(folder.glob("*.md")):

        with open(file, "r", encoding="utf-8") as f:

            documents.append(
                {
                    "filename": file.name,
                    "content": f.read(),
                }
            )

    return documents


def load_document_by_name(filename, doc_folder="docs"):
    """
    Load a single Markdown document by filename.

    Example:
        load_document_by_name("01_rag_fundamentals.md")
    """

    path = Path(doc_folder) / filename

    if not path.exists():
        return None

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":

    docs = load_documents()

    print(f"\nLoaded {len(docs)} documents:\n")

    for doc in docs:
        print(f"✅ {doc['filename']}")

    print("\nTesting single document loader...\n")

    sample = load_document_by_name("01_rag_fundamentals.md")

    if sample:
        print(sample[:300])
    else:
        print("Document not found.")