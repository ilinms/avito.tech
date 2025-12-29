import time
from pages.issues_page import IssuesPage

def test_filter_issues_by_status(page):
    issues_page = IssuesPage(page)
    issues_page.open()

    issues_page.filter_by_status("InProgress")

    assert issues_page.is_status_filter_applied("InProgress")
