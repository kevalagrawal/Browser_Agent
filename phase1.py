from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch browser
    browser = p.chromium.launch(headless=False, slow_mo=300)
    
    # Create a new page
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.bing.com")
    page2 = context.new_page()
    page2.goto("https://www.microsoft.com")
    
    # Go to a website
    
    # Wait for page to load
    page.wait_for_load_state("networkidle")
    
    # Print page title
    print("Page title is:", page.title())
    
    # Wait so you can observe
    input("Press Enter to close browser...")
    
    # Close browser
    browser.close()