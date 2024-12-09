# Suno Automation Project

## Project Overview
This project automates key interactions with the Suno platform, allowing users to:
1. Log in using Google credentials.
2. Submit a song generation request with customizable parameters.
3. Monitor the status of the song generation until completion.

The project leverages Python and key libraries such as Playwright, HTTPX, and dotenv for seamless automation.

---

## Prerequisites
Ensure the following tools and libraries are installed:
1. **Python**: Version 3.8 or higher.
2. **Google Chrome/Chromium**: Required for browser automation with Playwright.
3. **Python Packages**:
   Install the required dependencies:
   ```bash
   pip install playwright httpx python-dotenv

Directory structure

├── login.py          # Automates login to Suno with Google
├── generate_song.py  # Sends a song generation request
├── check_status.py   # Monitors the status of song generation
├── main.py           # Orchestrates the entire workflow
├── .env              # Environment variables for dynamic inputs
├── session.json      # Stores the session state after login

Environment Variables
Create a .env file in the project root to store sensitive data and dynamic inputs:
# Google account credentials
EMAIL=your_google_email
PASSWORD=your_google_password

# Song generation payload
SONG_TITLE=My First Song
SONG_STYLE=Pop
SONG_DURATION=120

# Optional: Predefined song UUID for status checking
SONG_UUID=optional_song_uuid


Usage Instructions
Step 1: Run Login Process
Run the login.py script to log in and save the session:

bash
Copy code
python login.py
This logs in using your Google credentials provided in .env.
A session file (session.json) is created to store session data.
Step 2: Generate a Song
Run the generate_song.py script to create a song:

bash
Copy code
python generate_song.py
It reads the session from session.json and sends a POST request to the Suno API with the payload from .env.
The response contains the song_uuid, which is required for status monitoring.
Step 3: Check Song Status
Run the check_status.py script to monitor the status of the song:

bash
Copy code
python check_status.py
It polls the status endpoint using the song_uuid and displays the current status until the song is completed or fails.
Step 4: Full Workflow
Run the main.py script to execute the entire process sequentially:

bash
Copy code
python main.py
Automates login, song generation, and status checking in one go.