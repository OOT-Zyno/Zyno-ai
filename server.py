from fastapi import FastAPI
import requests
import os

app = FastAPI()

API_KEY = os.getenv("API_KEY")

@app.get("/")
def home():
    return {"status": "Zyno AI running"}

@app.get("/chat")
def chat(q: str):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {"text": q}
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    try:
        result = response.json()
        return {
            "response": result["candidates"][0]["content"]["parts"][0]["text"]
        }
    except:
        return {
            "response": "Error: API issue",
            "full_error": response.text
        }
