from pages.elements_page import ElementsPage
from pages.demoqa import DemoQa


def test_navigation(browser):
    demopage = DemoQa(browser)
    elements_page = ElementsPage(browser)

    demopage.visit()
    demopage.btn_elements.click()
    elements_page.refresh()
    browser.refresh()
    browser.back()
    browser.forward()
    assert elements_page.equal_url()


