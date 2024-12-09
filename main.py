import asyncio
from login import login_to_suno
from generate_song import generate_song
from check_status import check_status

async def main():
    print("Starting Suno Automation...")
    
    # Step 1: Login and save the session
    print("Logging in to Suno...")
    await login_to_suno()

    # Step 2: Generate a song
    print("Generating a song...")
    song_uuid = await generate_song()
    if not song_uuid:
        print("Error: Unable to generate song UUID.")
        return

    # Step 3: Check the status of the song generation
    print(f"Checking the status of song UUID: {song_uuid}")
    await check_status(song_uuid)

    print("Suno Automation completed successfully.")

if __name__ == "__main__":
    asyncio.run(main())
