from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://demoqa.com/text-box")

    page.fill("#userName", "Archana")
    page.fill("#userEmail", "archanatest.com")
    page.fill("#currentAddress", "Hyderabad")
    page.fill("#permanentAddress", "Hyderabad")

    page.locator("#submit").scroll_into_view_if_needed()
    page.click("#submit", force=True)

    email_box = page.locator("#userEmail")
    class_value = email_box.get_attribute("class")

    if "field-error" in class_value:
        print("NEGATIVE TEST PASSED (Error shown)")
    else:
        print("NEGATIVE TEST FAILED (No error shown)")

    page.wait_for_timeout(10000)
    browser.close()

