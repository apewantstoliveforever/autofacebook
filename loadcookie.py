from selenium import webdriver
import pickle
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

options = Options()
options.add_argument("start-maximized")
s = Service("/usr/lib/chromium-browser/chromedriver")
browser = webdriver.Chrome(options=options, service= s)
browser.get("https://www.facebook.com/")

cookies = pickle.load(open('foreveralone16082003@gmail.com.pkl','rb'))
for cookie in cookies:
    browser.add_cookie(cookie)

browser.get("https://www.facebook.com/")

time.sleep(5)
