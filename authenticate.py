from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    
    # 1️⃣ First time: create context and save storage state
    context = browser.new_context()
    
    page = context.new_page()
    page.goto("https://www.bing.com")
    
    print("Please log in manually to your Microsoft account, then press Enter here...")
    input()
    
    # Save session to file
    context.storage_state(path="ms_session.json")
    print("Session saved!")
    
    browser.close()