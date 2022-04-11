from selenium import webdriver
import time
import pickle
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

user_email = input('your email ')
user_password = input('your password' )

options = Options()
options.add_argument("start-maximized")
s = Service("/usr/lib/chromium-browser/chromedriver")
browser = webdriver.Chrome(options=options, service= s)
browser.get("https://www.facebook.com/")

username = browser.find_element(by= By.ID, value= 'email')
password = browser.find_element(by= By.ID, value= 'pass')
username.send_keys(user_email)
password.send_keys(user_password)
login_button = browser.find_element(by= By.CSS_SELECTOR, value='button[data-testid="royal_login_button"]')
login_button.click()
time.sleep(5)
pickle.dump(browser.get_cookies(), open(f'{user_email}.pkl', 'wb'))
time.sleep(5)
browser.close()