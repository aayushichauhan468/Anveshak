from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("GROQ_API_KEY")

if key:
 print("Groq key loaded successfully. Starts with:", key[:10], "...")
else:
 print("No key found — check your .env file.")