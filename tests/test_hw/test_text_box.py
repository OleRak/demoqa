from pages.text_box import TextBox
import time


def test_text_box(browser):
    text_box = TextBox(browser)

    text_box.visit()
    text_box.full_name.send_keys("Rak")
    time.sleep(2)
    text_box.current_address.send_keys("54")
    time.sleep(2)
    text_box.btn_submit.click_force()
    #assert text_box.border.check_count_elements(count=2) не знаю как подобрать селектор к элементам, которые надо считать
