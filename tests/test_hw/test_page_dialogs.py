from pages.modal_dialogs import ModalDialogs
from pages.demoqa import DemoQa


def test_page_dialogs(browser):
    modal_dialogs = ModalDialogs(browser)

    modal_dialogs.visit()
    assert modal_dialogs.btn_light.check_count_elements(count=5)


def test_navigational_mode(browser):
    modal_dialogs = ModalDialogs(browser)
    demopage = DemoQa(browser)

    modal_dialogs.visit()
    modal_dialogs.refresh()
    modal_dialogs.icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert demopage.equal_url()
    assert demopage.title.exist()
    browser.set_window_size(1000, 1000)







