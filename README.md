# Автоматизация тестирования Avito Tech Internship

## Описание проекта

Данный проект содержит автоматизированные UI-тесты для веб-приложения управления задачами, предоставленного в рамках тестового задания Avito Tech Internship.

Цель проекта — автоматизировать основные пользовательские сценарии и подтвердить их корректную работу с помощью автотестов.

Автоматизированы следующие сценарии:
- Создание задачи
- Открытие карточки задачи
- Поиск задачи
- Переход на доску проекта из карточки задачи
- Открытие доски со страницы проектов
- Фильтрация задач по статусу
- Фильтрация задач по доске проекта

---

## Используемые технологии

- Python 3.11
- Pytest
- Playwright (sync API)
- Page Object Model

---

## Установка и запуск проекта

1. Клонировать репозиторий:
git clone <repository_url>
cd <project_folder>

2. Создать виртуальное окружение:
python -m venv venv

3. Активировать виртуальное окружение (Windows):
venv\Scripts\activate

4. Установить зависимости:
pip install -r requirements.txt

5. Установить браузеры Playwright:
playwright install

---

## Структура проекта

pages/
- issues_page.py — Page Object основной страницы

tests/
- test_create_issue.py — создание задачи
- test_open_issue.py — открытие карточки задачи
- test_search_issue.py — поиск задачи по названию
- test_go_to_board_from_issue_card.py — переход на доску из карточки задачи
- test_open_board_from_projects.py — открытие доски со страницы проектов
- test_filter_issues_by_status.py — фильтрация задач по статусам (InProgressб, Backlog, Done)
- test_filter_issues_by_board.py — фильтрация задач по всем доскам проектов

pytest.ini  
README.md  
TESTCASES.md  
BUGS.md  

---

## Запуск тестов

Запуск всех тестов:
python -m pytest --headed --browser chromium -vv

Запуск конкретного теста:
python -m pytest tests/test_create_issue.py --headed --browser chromium -vv

Запуск с замедлением для визуального контроля:
python -m pytest --headed --browser chromium --slowmo 200 -vv

---

## Дополнительные материалы

- TESTCASES.md — описание тест-кейсов, которые были автоматизированы
- BUGS.md — баг-репорты, выявленные в ходе тестирования (при наличии)

---

## Заключение

В рамках задания были автоматизированы основные пользовательские сценарии приложения. 
Все тесты успешно выполняются и подтверждают корректную работу функциональности.
