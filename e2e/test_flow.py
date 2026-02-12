from playwright.sync_api import sync_playwright


def test_calculator_e2e():
    with sync_playwright() as p:
        # W CI uruchomimy to w trybie headless
        browser = p.chromium.launch()
        page = browser.new_page()

        # Zakładamy, że aplikacja działa na localhost:8000
        page.goto("http://localhost:8000")

        # Scenariusz: 2 + 3 = 5
        page.click("text=2")
        page.click("text=+")
        page.click("text=3")
        page.click("text==")

        # Czekamy na wynik z API
        page.wait_for_function("document.getElementById('display').value == '5'")

        val = page.input_value("#display")
        assert val == "5"

        browser.close()