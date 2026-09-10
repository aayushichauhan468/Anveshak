import chromadb

   # This creates a local folder called 'chroma_data' to store everything.
   # No server, no internet needed — it's just files on your computer.
client = chromadb.PersistentClient(path="chroma_data")

collection = client.get_or_create_collection(name="code_doc_pairs")


def store_item(item_id: str, embedding: list, metadata: dict):
       """Saves one embedding + its metadata into ChromaDB."""
       collection.add(
           ids=[item_id],
           embeddings=[embedding],
           metadatas=[metadata],
       )


def find_closest(embedding: list, n_results: int = 1):
       """Finds the most similar stored item(s) to the given embedding."""
       return collection.query(
           query_embeddings=[embedding],
           n_results=n_results,
       )