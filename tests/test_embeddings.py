from sentence_transformers import SentenceTransformer

print("Loading model (first run downloads it, may take a minute)...")
model = SentenceTransformer("all-MiniLM-L6-v2")

text1 = "Logs the user in using their account_id and password."
text2 = "Logs the user in using their user_id and password."

embeddings = model.encode([text1, text2])
print("Embedding generated successfully.")
print("Shape of each embedding:", embeddings[0].shape)