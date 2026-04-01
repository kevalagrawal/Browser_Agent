from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=150)
    context = browser.new_context()
    page = context.new_page()
    
    print("Opening Bing...")
    page.goto("https://www.bing.com")
    
    print("Waiting for search box...")
    search_box = page.locator("#sb_form_q")
    search_box.wait_for(timeout=10000)
    
    print("Clicking search box...")
    search_box.click()
    
    print("Typing...")
    query = "weather in Ahmedabad"
    
    for char in query:
        search_box.type(char)
        time.sleep(0.08)
    
    print("Pressing Enter...")
    page.keyboard.press("Enter")
    
    print("Waiting for results...")
    page.wait_for_load_state("networkidle")
    
    input("Press Enter to close...")
    browser.close()