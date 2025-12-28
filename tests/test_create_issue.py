from pages.issues_page import IssuesPage


def test_create_issue(page):
    issues_page = IssuesPage(page)

    issues_page.open()

    title = "Test issue"
    description = "Test description"

    issues_page.create_issue(title, description)

    assert issues_page.is_issue_visible(title)
