import time
from pages.issues_page import IssuesPage


def test_search_issue(page):
    issues_page = IssuesPage(page)
    issues_page.open()

    title = f"autotest issue {int(time.time())}"
    description = "autotest description"

    issues_page.create_issue(title, description)
    issues_page.search_issue(title)

    assert issues_page.is_issue_in_list(title)
