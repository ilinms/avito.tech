import pytest
from pages.issues_page import IssuesPage


@pytest.mark.parametrize("board", [
    "Редизайн карточки товара",
    "Оптимизация производительности",
    "Рефакторинг API",
    "Миграция на новую БД",
    "Автоматизация тестирования",
    "Переход на Kubernetes"
])
def test_filter_issues_by_board(page, board):
    issues_page = IssuesPage(page)
    issues_page.open()

    issues_page.filter_by_board(board)

    assert issues_page.is_board_filter_applied_correctly(board), \
        f"Фильтр по доске '{board}' не работает корректно"

