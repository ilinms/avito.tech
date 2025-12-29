from pages.issues_page import IssuesPage


def test_filter_issues_by_board(page):
    issues_page = IssuesPage(page)
    issues_page.open()

    issues_page.filter_by_board("Рефакторинг API")

    assert issues_page.is_board_filter_applied("Рефакторинг API")
