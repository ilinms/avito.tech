from pages.issues_page import IssuesPage


def test_go_to_board_from_issue_card(page):
    issues_page = IssuesPage(page)
    issues_page.open()

    title = f"autotest issue {int(time.time())}"
    description = "autotest description"

    issues_page.create_issue(title, description)
    issues_page.open_issue(title)
    issues_page.go_to_board_from_issue()

    assert issues_page.is_board_opened()
