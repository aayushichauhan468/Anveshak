from sentence_transformers import SentenceTransformer

   # Load once, reuse everywhere — loading this repeatedly is slow
_model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embedding(text: str):
       """Converts a piece of text into a numeric vector (embedding)."""
       return _model.encode(text).tolist()