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

    def open_issue(self, title: str):
        self.page.get_by_text(title).click()

    def is_issue_card_opened(self) -> bool:
        self.page.get_by_role("heading", name="Редактирование задачи").wait_for(timeout=5000)
        return True

    def search_issue(self, text: str):
        self.page.get_by_placeholder("Поиск").fill(text)
        self.page.wait_for_timeout(500)

    def is_issue_in_list(self, title: str) -> bool:
        self.page.get_by_text(title).wait_for(timeout=5000)
        return True

    def go_to_board(self):
        self.page.get_by_role("link", name="Перейти на доску").click()

    def open_projects(self):
        self.page.get_by_role("link", name="Проекты").click()

    def open_project_board(self, project_name):
        project_card = self.page.get_by_role("heading", name=project_name).locator("..").locator("..")
        project_card.get_by_role("link", name="Перейти к доске").click()

    def is_board_opened(self):
        self.page.wait_for_url("**/board/**", timeout=5000)
        return True

    def go_to_board_from_issue(self):
        self.page.get_by_role("link", name="Перейти на доску").click()












