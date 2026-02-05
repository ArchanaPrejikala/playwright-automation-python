from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://demoqa.com/text-box")

    page.fill("#userName", "Archana")
    page.fill("#userEmail", "archana@test.com")
    page.fill("#currentAddress", "Hyderabad")
    page.fill("#permanentAddress", "Hyderabad")
    
    page.locator("#submit").scroll_into_view_if_needed()
    page.click("#submit", force=True)
 
    page.wait_for_selector("#output")
    result_text = page.locator("#output").inner_text()
    if "Archana" in result_text and "archana@test.com" in result_text:
        print("MANUAL TO AUTO TEST PASSED")
    else:
        print("MANUAL TO AUTO TEST FAILED")
    page.wait_for_timeout(10000)
    browser.close()