from playwright.sync_api import Page


class IssuesPage:
    URL = "https://avito-tech-internship-psi.vercel.app/"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.URL)
        self.page.wait_for_load_state("networkidle")

    def create_issue(self, title: str, description: str):
        # Нажимаем кнопку "Создать задачу"
        self.page.get_by_text("Создать задачу", exact=True).first.click()

        # Заполняем поля в диалоге
        self.page.get_by_label("Title", exact=True).fill(title)
        self.page.get_by_label("Description", exact=True).fill(description)

        # Нажимаем кнопку сохранения
        self.page.get_by_role("button", name="Create").click()

    def is_issue_visible(self, title: str) -> bool:
        return self.page.get_by_text(title).is_visible()
