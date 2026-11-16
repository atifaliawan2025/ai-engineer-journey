from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client()

response = client.models.generate_content(
   model="gemini-3.8-flash",
    contents="Explain RAG in two sentences.",
)

print(response.text)
print(response.usage_metadata)