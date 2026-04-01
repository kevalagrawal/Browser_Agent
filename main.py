from playwright.sync_api import sync_playwright
import time
import random
import os

# --------------------------
# Configuration
# --------------------------
SESSION_FILE = "ms_session.json"
NUM_SEARCHES = 30

subjects = ["Python", "AI", "Microsoft", "history", "weather", "technology", "space", "finance", "travel", "science"]
keywords = ["tutorial", "news", "guide", "facts", "trends", "tips", "examples"]
modifiers = ["in Ahmedabad", "2026", "for beginners", "latest", "today", "easy steps"]

used_queries = set()

# --------------------------
# Query Generator
# --------------------------
def generate_query():
    return f"{random.choice(subjects)} {random.choice(keywords)} {random.choice(modifiers)}"

def get_unique_query():
    while True:
        query = generate_query()
        if query not in used_queries:
            used_queries.add(query)
            return query

# --------------------------
# Main Automation
# --------------------------
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=100)
    
    # Load session
    if os.path.exists(SESSION_FILE):
        print("Loading saved session...")
        context = browser.new_context(storage_state=SESSION_FILE)
    else:
        print("No session found. Please log in manually...")
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.bing.com")
        input("After logging in, press Enter here...")
        context.storage_state(path=SESSION_FILE)

    # 🟢 Start with first tab
    current_page = context.new_page()
    current_page.goto("https://www.bing.com")

    for i in range(NUM_SEARCHES):
        query = get_unique_query()
        print(f"\nSearch {i+1}: {query}")
        
        # Open new tab
        new_page = context.new_page()
        new_page.goto("https://www.bing.com")
        
        # Perform search on new tab
        search_box = new_page.locator("#sb_form_q")
        search_box.wait_for(timeout=10000)
        
        search_box.click()
        search_box.fill("")
        search_box.type(query, delay=80)
        
        new_page.keyboard.press("Enter")
        new_page.wait_for_load_state("networkidle")
        
        # 👁️ View results
        view_time = random.uniform(2, 4)
        print(f"Viewing results for {round(view_time,2)} seconds...")
        time.sleep(view_time)
        
        # ❌ Close previous tab
        current_page.close()
        print("Previous tab closed.")
        
        # 🔁 Switch reference
        current_page = new_page
        
        # ⏱️ Delay before next iteration
        delay = random.uniform(1.5, 3.5)
        print(f"Waiting {round(delay,2)} seconds...")
        time.sleep(delay)

    input("\nAll searches completed. Press Enter to close browser...")
    browser.close()