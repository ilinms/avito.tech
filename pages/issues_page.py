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

    def change_status(self, status: str):
        self.page.get_by_role("combobox", name="Статус").click()
        self.page.get_by_role("option", name=status).click()

    def close_issue_card(self):
        self.page.keyboard.press("Escape")

    def filter_by_status(self, status: str):
        self.page.locator('div[role="combobox"]').first.click()
        self.page.get_by_role("option", name=status).click()

    def is_status_filter_applied(self, status: str) -> bool:
        actual_status = self.get_status_filter_text()
        return actual_status == status

    def filter_by_board(self, board_name: str):
        self.page.locator('div[role="combobox"]').nth(1).click()
        self.page.get_by_role("option", name=board_name).click()

    def is_board_filter_applied(self, board_name: str) -> bool:
        return self.page.locator(
            'div[role="combobox"]'
        ).nth(1).get_by_text(board_name).is_visible()

    def get_status_filter_text(self) -> str:
        chip_label = self.page.locator(".MuiChip-label").first
        return chip_label.inner_text().strip()

    def is_status_filter_applied(self, status: str) -> bool:
        actual_status = self.get_status_filter_text()
        return actual_status == status

    def are_all_issues_have_status(self, status: str) -> bool:
        status_chips = self.page.locator('div.MuiChip-root')

        if status_chips.count() == 0:
            return False

        for i in range(status_chips.count()):
            chip_text = status_chips.nth(i).inner_text().strip()
            if chip_text != status:
                print(f"Найден статус '{chip_text}', а ожидается '{status}'")
                return False

        return True

    def is_status_filter_applied_correctly(self, status: str) -> bool:
        filter_applied = self.is_status_filter_applied(status)
        list_filtered = self.are_all_issues_have_status(status)

        return filter_applied and list_filtered

























