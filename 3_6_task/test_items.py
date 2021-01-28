from selenium import webdriver
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_shop(browser):
    #browser = webdriver.Chrome(options=options)
    browser.get(link)
    button = browser.find_element_by_css_selector('button.btn-add-to-basket')
    assert button.is_enabled(), f"Button '{button.text}' is not active right now"
    print("You have clicked on the '" + button.text + "' !")
