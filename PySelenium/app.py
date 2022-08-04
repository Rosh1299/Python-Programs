from selenium import webdriver


browser = webdriver.Chrome()
browser.get("https://github.com/login")


# username_box = browser.find_element_by_id("login_field")
username_box = browser.find_element(by="id", value="login_field")
username_box.send_keys("roshansagvekar1299@gmail.com")
password_box = browser.find_element(by="id", value="password")
password_box.send_keys("Rosh@1299")
password_box.submit()

assert "RoshanSagvekar" in browser.page_source
profile_link = browser.find_element_by_class_name("user-profile-link")
link_label = profile_link.get_attribute("innerHTML")
assert "RoshanSagvekar" in link_label

browser.quit()

# Automating facebook
"""
browser = webdriver.Chrome()
browser.get("https://www.facebook.com/")
username_box = browser.find_element(by="id", value="email")
username_box.send_keys("")
password_box = browser.find_element(by="id", value="pass")
password_box.send_keys("")
password_box.submit()
"""
