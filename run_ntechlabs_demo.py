import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://ntechlabs.mindriserstech.com/")
    page.get_by_role("img", name="Hero Image").click()
    page.get_by_role("img", name="Mobile & Web App Developments").click()
    page.get_by_role("button", name="Contact us", exact=True).click()
    page.get_by_role("textbox", name="Enter Your Name").click()
    page.get_by_role("textbox", name="Enter Your Name").fill("shyam singh")
    page.get_by_role("textbox", name="Enter Your Email").click()
    page.get_by_role("textbox", name="Enter Your Email").fill("shyam2121@gmail.com")
    page.get_by_role("textbox", name="Enter Your Phone").click()
    page.get_by_role("textbox", name="Enter Your Phone").fill("9845484844")
    page.locator("input[name=\"date\"]").fill("2026-04-26")
    page.get_by_role("textbox", name="Enter Your Message").click()
    page.get_by_role("textbox", name="Enter Your Message").fill("bakjwas companuy xa kei kam xainan vanera kasle vaneko hola taba la tminai gar ak garxau ")
    page.get_by_role("button", name="Send").click()


    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
