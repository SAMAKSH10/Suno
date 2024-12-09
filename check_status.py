import httpx
import asyncio
from dotenv import load_dotenv
import os
import json


# Load environment variables
load_dotenv()

async def check_status(uuid=None):
    if uuid is None:
        uuid = os.getenv("SONG_UUID")
    if not uuid:
        raise ValueError("Song UUID not provided or set in .env file.")

    with open("session.json", "r") as f:
        session_data = json.load(f)

    cookies = {cookie["name"]: cookie["value"] for cookie in session_data["cookies"]}
    url = f"https://studio-api.prod.suno.com/api/song/status/{uuid}"

    async with httpx.AsyncClient(cookies=cookies) as client:
        while True:
            response = await client.get(url)
            status_data = response.json()
            print("Current Status:", status_data)
            if status_data.get("status") == "completed":
                print("Song generation completed!")
                break
            elif status_data.get("status") == "failed":
                print("Generation failed.")
                break
            await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(check_status())
