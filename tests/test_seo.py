from pages.demoqa import DemoQa


def test_seo(browser):
    demopage = DemoQa(browser)

    demopage.visit()
    assert browser.title == "DEMOQA"

