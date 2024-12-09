import asyncio
from playwright.async_api import async_playwright
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

async def login_to_suno():
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    if not email or not password:
        raise ValueError("Email or password not set in the .env file.")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        # Navigate to Suno login page
        await page.goto("https://suno.com/")
        await page.click("text=Sign In")
        await page.click("button:has-text('Sign in with Google')")
        await page.fill('input[type="email"]', email)
        await page.click("button:has-text('Next')")
        await asyncio.sleep(1)
        await page.fill('input[type="password"]', password)
        await page.click("button:has-text('Next')")

        await page.wait_for_url("https://suno.com/dashboard")
        await context.storage_state(path="session.json")
        await browser.close()
        print("Login successful and session saved.")

if __name__ == "__main__":
    asyncio.run(login_to_suno())
