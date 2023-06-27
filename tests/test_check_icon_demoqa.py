from pages.demoqa import DemoQa

def test(browser):

    demopage = DemoQa(browser)
    demopage.visit()
    demopage.icon.click()
    assert demopage.equal_url()
    assert demopage.icon.exist()



