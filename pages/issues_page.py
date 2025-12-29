from playwright.sync_api import Page, expect


class IssuesPage:
    URL = "https://avito-tech-internship-psi.vercel.app/"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.URL)
        self.page.wait_for_load_state("networkidle")

    def create_issue(self, title: str, description: str):
        self.page.get_by_text("Создать задачу", exact=True).first.click()

        self.page.get_by_label("Название").fill(title)
        self.page.get_by_label("Описание").fill(description)

        comboboxes = self.page.get_by_role("combobox")

        comboboxes.nth(0).click()
        self.page.get_by_role("option", name="Рефакторинг API").click()

        comboboxes.nth(1).click()
        self.page.get_by_role("option", name="Low").click()

        comboboxes.nth(3).click()
        self.page.get_by_role("option", name="Илья Романов").click()

        self.page.get_by_role("button", name="Создать").click()

    def is_issue_visible(self, title: str) -> bool:
        self.page.get_by_text(title).wait_for(timeout=5000)
        return True

