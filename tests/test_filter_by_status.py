import pytest
from pages.issues_page import IssuesPage

@pytest.mark.parametrize("status", ["InProgress", "Backlog", "Done"])
def test_filter_issues_by_status(page, status):
    issues_page = IssuesPage(page)
    issues_page.open()

    issues_page.filter_by_status(status)

    assert issues_page.is_status_filter_applied_correctly(status), \
        f"Фильтр по статусу '{status}' не работает корректно"
