from pages.elements_page import ElementsPage
import time


def test_not_visible_btn_sider(browser):
    elements_page = ElementsPage(browser)

    elements_page.visit()
    assert elements_page.btn_sidebar_first_textbox.visible()
    elements_page.btn_sidebar_first.click()
    time.sleep(2)
    assert not elements_page.btn_sidebar_first_textbox.visible()
