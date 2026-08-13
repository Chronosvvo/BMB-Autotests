import pytest
from playwright.sync_api import Page
from pages.home_page import MainPage
import allure
from pathlib import Path


@pytest.fixture
def page_ru(page: Page) -> Page:
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto("/ru")
    return page

@pytest.fixture
def home_page(page_ru: MainPage) -> MainPage:
    return MainPage(page_ru)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Сохраняем результат теста для последующих hook'ов
    setattr(item, f"rep_{report.when}", report)

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            screenshot = page.screenshot()

            allure.attach(
                screenshot,
                name="Screenshot",
                attachment_type=allure.attachment_type.PNG,
            )


@pytest.hookimpl(trylast=True)
def pytest_runtest_teardown(item, nextitem):
    report = getattr(item, "rep_call", None)

    if not report or not report.failed:
        return

    output_path = item.funcargs.get("output_path")

    if not output_path:
        return

    trace_path = Path(output_path) / "trace.zip"

    if trace_path.exists():
        allure.attach.file(
            str(trace_path),
            name="Playwright Trace",
            attachment_type="application/zip",
        )