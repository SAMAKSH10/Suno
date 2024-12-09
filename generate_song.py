import httpx
import json
from dotenv import load_dotenv
import os
import asyncio

# Load environment variables
load_dotenv()

async def generate_song():
    with open("session.json", "r") as f:
        session_data = json.load(f)

    cookies = {cookie["name"]: cookie["value"] for cookie in session_data["cookies"]}
    headers = {"Content-Type": "application/json"}

    # Dynamic payload from environment variables
    title = os.getenv("SONG_TITLE", "Default Song")
    style = os.getenv("SONG_STYLE", "Pop")
    duration = int(os.getenv("SONG_DURATION", 120))

    url = "https://studio-api.prod.suno.com/api/song/generate"
    payload = {
        "title": title,
        "style": style,
        "duration": duration,
    }

    async with httpx.AsyncClient(cookies=cookies) as client:
        response = await client.post(url, json=payload, headers=headers)
        response_data = response.json()
        print("Song generation response:", response_data)
        return response_data.get("song_uuid")

if __name__ == "__main__":
    asyncio.run(generate_song())
