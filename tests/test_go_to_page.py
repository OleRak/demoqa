from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

def test_go_to_page_elements(browser):

    demopage = DemoQa(browser)
    elements_page = ElementsPage(browser)

    demopage.visit()
    assert demopage.equal_url()
    demopage.btn_elements.click()
    assert elements_page.equal_url()


