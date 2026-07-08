import re


def chunk_document(document):
    """
    Split a Markdown document into semantic chunks based on headings.

    Args:
        document: {
            "filename": "...",
            "content": "..."
        }

    Returns:
        List of chunks.
    """

    filename = document["filename"]
    content = document["content"]

    # Split on level-2 headings (## ...)
    sections = re.split(r"(?=^## )", content, flags=re.MULTILINE)

    chunks = []

    chunk_id = 1

    for section in sections:

        section = section.strip()

        if not section.startswith("##"):
            continue

        lines = section.splitlines()

        heading = lines[0].replace("##", "").strip()

        text = "\n".join(lines[1:]).strip()

        chunks.append(
            {
                "source": filename,
                "section": heading,
                "chunk_id": chunk_id,
                "text": text,
                "id": f"{filename}_{chunk_id}"
            }
        )

        chunk_id += 1

    return chunks


def chunk_documents(documents):

    all_chunks = []

    for document in documents:
        all_chunks.extend(chunk_document(document))

    return all_chunks

if __name__ == "__main__":

    from ingest import load_documents

    docs = load_documents()

    chunks = chunk_documents(docs)

    print(f"\nCreated {len(chunks)} chunks.\n")

    for chunk in chunks[:5]:

        print("=" * 60)

        print("SOURCE :", chunk["source"])

        print("SECTION:", chunk["section"])

        print("CHUNK  :", chunk["chunk_id"])

        print()

        print(chunk["text"][:250])

        print()