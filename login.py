import os
import time
from common_functions import close_multiple_windows
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

# To clear console
os.system('cls')

chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
chrome.get("https://www.saucedemo.com/")
chrome.maximize_window()

time.sleep(5)

# ========== LOGIN TESTING ===============

username_field=chrome.find_element(By.ID,'user-name')
username_field.send_keys("standard_user")

time.sleep(5)

password_field=chrome.find_element(By.ID,'password')
password_field.send_keys("secret_sauce")

time.sleep(5)

login_button=chrome.find_element(By.ID,'login-button')
login_button.click()

print("Login Test case passed")

# ============ HOME PAGE TESTING ===============
time.sleep(10)


# ============ HOME PAGE CARDS TESTING ===============

card_one_title=chrome.find_element(By.XPATH,'//*[@id="item_4_title_link"]')
card_one_title.click()
print("Card title click test case passed")
time.sleep(5)
chrome.find_element(By.ID,"back-to-products").click()
time.sleep(5)

card_two_img=chrome.find_element(By.XPATH,'//*[@id="item_0_img_link"]')
card_two_img.click()
print("Card image click test case passed")
time.sleep(5)
chrome.find_element(By.ID,"back-to-products").click()
time.sleep(5)

# ============ HOME PAGE CARDS ADD TO CART BTN TESTING ===============
card_one_btn=chrome.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-backpack"]')
card_one_btn.click()
time.sleep(2)

card_two_btn=chrome.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-bike-light"]')
card_two_btn.click()
time.sleep(2)

card_three_btn=chrome.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-bike-light"]')
card_three_btn.click()
time.sleep(2)

card_four_btn=chrome.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-bike-light"]')
card_four_btn.click()
time.sleep(2)

# ============ HOME PAGE CARDS REMOVE BTN TESTING ===============

# time.sleep(10)
chrome.quit()
exit()

# ============ SORTING TESTING ===============

# a-z sorting
sorting_dropdown = Select(chrome.find_element(By.CLASS_NAME,'product_sort_container'))
sorting_dropdown.select_by_value("az")
time.sleep(10)

# z-a sorting
sorting_dropdown = Select(chrome.find_element(By.CLASS_NAME,'product_sort_container'))
sorting_dropdown.select_by_value("za")
time.sleep(10)

# low-high sorting
sorting_dropdown = Select(chrome.find_element(By.CLASS_NAME,'product_sort_container'))
sorting_dropdown.select_by_value("lohi")
time.sleep(10)


# high-low sorting
sorting_dropdown = Select(chrome.find_element(By.CLASS_NAME,'product_sort_container'))
sorting_dropdown.select_by_value("hilo")
time.sleep(10)


# time.sleep(10)
# chrome.quit()

# ============ FOOTER LINKS TESTING ===============
time.sleep(5)
chrome.execute_script("window.scrollBy(0,1000);")
time.sleep(5)

twitter_link=chrome.find_element(By.XPATH,'//*[@id="page_wrapper"]/footer/ul/li[1]/a')
twitter_link.click()

time.sleep(10)
close_multiple_windows(chrome)
time.sleep(10)

facebook_link=chrome.find_element(By.XPATH,'//*[@id="page_wrapper"]/footer/ul/li[2]/a')
facebook_link.click()

time.sleep(10)
close_multiple_windows(chrome)
time.sleep(10)

linkedin_link=chrome.find_element(By.XPATH,'//*[@id="page_wrapper"]/footer/ul/li[3]/a')
linkedin_link.click()

time.sleep(10)
close_multiple_windows(chrome)

# time.sleep(10)
# chrome.quit()
