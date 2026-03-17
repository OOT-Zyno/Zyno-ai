from fastapi import FastAPI
import requests
import os

app = FastAPI()

API_KEY = "AIzaSyBCAnWe9upaE46luWLE8gabgSpz2wov-Ds"

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
                    {
                        "text": f"You are Zyno AI created by Madhav. Talk in Hinglish.\nUser: {q}"
                    }
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    res = response.json()

    try:
        reply = res["candidates"][0]["content"]["parts"][0]["text"]
    except:
        reply = "Error: API issue"

    return {"response": reply}
