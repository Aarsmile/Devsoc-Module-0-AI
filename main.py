
import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
with open("text.txt", "r") as file:
    questions = file.readlines()

responses = []

client = genai.Client(api_key=api_key)
print("Client made")
for question in questions:
    print("Processing:", question.strip(), flush=True)
    response = client.models.generate_content(
    model = "gemini-3.5-flash-lite",
    contents = question
    )
    responses.append({
    "question": question.strip(),
    "answer": response.text
})

with open("responses.json", "w") as file:
    json.dump(responses, file, indent=4)