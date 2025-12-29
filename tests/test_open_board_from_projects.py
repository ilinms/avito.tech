from pages.issues_page import IssuesPage


def test_open_board_from_projects(page):

    issues_page = IssuesPage(page)
    issues_page.open()

    issues_page.open_projects()
    issues_page.open_project_board("Рефакторинг API")

    assert issues_page.is_board_opened()
