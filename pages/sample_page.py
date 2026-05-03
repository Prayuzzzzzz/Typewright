from playwright.sync_api import Page

class SamplePage:
    def __init__(self, page: Page):
        self.page = page
        self.contact_name = 'input[name="first_name"]'
        self.contact_email = 'input[name="email"]'
        self.contact_message = 'textarea[name="message"]'
        self.submit_button = 'input[type="submit"]'

    def goto_contact(self):
        self.page.goto("https://www.tukee.org.np/contact")

    def fill_sample_form(self, name, email, message):
        self.page.fill(self.contact_name, name)
        self.page.fill(self.contact_email, email)
        self.page.fill(self.contact_message, message)

    def submit_form(self):
        self.page.click(self.submit_button)