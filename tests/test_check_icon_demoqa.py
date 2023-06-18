from pages.demoqa import DemoQa

def test(browser):

    demopage = DemoQa(browser)
    demopage.visit()
    demopage.click_on_the_icon()
    assert demopage.equal_url()
    assert demopage.exist_icon()

    # browser.get("https://demoqa.com")
    # link = browser.find_element(By.CSS_SELECTOR, "#app > header > a")
    #
    # if link is None:
    #     print("Элемент не найден")
    # else:
    #     print("Элемент найден")

