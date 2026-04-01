from playwright.sync_api import sync_playwright
import time
import random
import os

queries = [
    "weather in Ahmedabad",
    "latest tech news",
    "Python automation tutorial",
    "history of India",
    "how AI works"
]

SESSION_FILE = "ms_session.json"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=100)
    
    # 🔐 Load session if exists, else create new
    if os.path.exists(SESSION_FILE):
        print("Loading saved session...")
        context = browser.new_context(storage_state=SESSION_FILE)
    else:
        print("No session found. Please log in manually...")
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.bing.com")
        
        input("After logging in, press Enter here...")
        
        # Save session
        context.storage_state(path=SESSION_FILE)
        print("Session saved!")
    
    # 🚀 Start search automation
    for i, query in enumerate(queries):
        print(f"Search {i+1}: {query}")
        
        # New tab for each query
        page = context.new_page()
        page.goto("https://www.bing.com")
        
        # Locate search box
        search_box = page.locator("#sb_form_q")
        search_box.wait_for(timeout=10000)
        
        # Type query
        search_box.click()
        search_box.fill("")
        search_box.type(query, delay=80)
        
        # Search
        page.keyboard.press("Enter")
        page.wait_for_load_state("networkidle")
        
        # Random delay
        delay = random.uniform(2, 5)
        print(f"Waiting {round(delay,2)} seconds...")
        time.sleep(delay)
    
    input("All searches done. Press Enter to close...")
    browser.close()