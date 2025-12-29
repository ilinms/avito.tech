import time
from pages.issues_page import IssuesPage


def test_create_issue(page):
    issues_page = IssuesPage(page)
    issues_page.open()

    title = f"autotest issue {int(time.time())}"
    description = "autotest description"

    issues_page.create_issue(title, description)

    assert issues_page.is_issue_visible(title)
