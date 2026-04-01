from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=300)
    
    # Create a browser context (like a real user session)
    context = browser.new_context()
    
    # First tab
    page1 = context.new_page()
    page1.goto("https://www.bing.com")
    
    # Second tab (same window)
    page2 = context.new_page()
    page2.goto("https://www.microsoft.com")
    
    input("Press Enter to close...")
    browser.close()