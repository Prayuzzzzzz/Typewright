import pytest
from playwright.sync_api import sync_playwright
from pages.sample_page import SamplePage

@pytest.fixture
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

def test_sample_form(browser):
    page_obj = SamplePage(browser)
    page_obj.goto_contact()
    page_obj.fill_sample_form(
        name="Zayne",
        email="test@example.com",
        message="This is a sample test message."
    )
    page_obj.submit_form()

    # Simple assertion
    assert "Thank you" in browser.content() or "success" in browser.content().lower()