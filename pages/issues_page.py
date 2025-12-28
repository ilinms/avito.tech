from playwright.sync_api import Page, expect


class IssuesPage:
    URL = "https://avito-tech-internship-psi.vercel.app/"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.URL)
        self.page.wait_for_load_state("networkidle")

    def create_issue(self, title: str, description: str):
        self.page.get_by_role("button", name="Создать задачу").click()
        self.page.get_by_label("Title").fill(title)
        self.page.get_by_label("Description").fill(description)
        self.page.get_by_role("button", name="Create").click()

    def is_issue_visible(self, title: str) -> bool:
        return self.page.get_by_text(title).is_visible()

    def open_issue(self, title: str):
        self.page.get_by_text(title).click()

    def search_issue(self, text: str):
        self.page.get_by_placeholder("Search").fill(text)

    def go_to_board(self):
        self.page.get_by_role("link", name="Board").click()
