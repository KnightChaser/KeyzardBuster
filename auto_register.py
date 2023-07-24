from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import random
from time import sleep

browser = webdriver.Chrome()

# 0. fake setitngs :p
options = webdriver.ChromeOptions()
options.add_argument("disable-gpu")   
options.add_argument("lang=ko_KR")    # fake plugin
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
 
# 1. Login
browser.get("https://keyzard.org/login")
keyzard_id = "XXXXXXXXXXXXXX"    # <--- Your Naver blog ID
keyzard_pw = "XXXXXXXXXXXXXX"    # <--- Your Naver blog password (same as your main Naver account)

browser.find_element("id", "id").send_keys(keyzard_id)
browser.find_element("id", "pw").send_keys(keyzard_pw)
browser.find_element("id", "loginBtn").click()

sleep(1)

# 2. Move to registration tab and register one by one, until it exhausts
browser.get("https://keyzard.org/nb")

file_path = "./url_list.txt"    # <--- Be sure that you first extracted all of your blog posts' URLs by running get_blog_post_urls.py

# first, get file line to calculate progress
with open(file_path, "r") as f:
    line_count = sum(1 for _ in f)

# second, proceed!
browser.execute_script("window.alert = function() {};")     # disable alert, it's very annoying to deal with Selenium.

try:
    with open(file_path, 'r') as file:
        progress = 1

        for line in file:

            sleep(random.uniform(1, 1.5))    # adjust this sleep() interval if you want, but don't lower it too much! The website would ban you.

            try_url = line.strip()
            browser.find_element("id", "blogUrl").send_keys(try_url)
            browser.find_element("id", "submit").click()

            print(f"Processed [{progress}/{line_count}]({round(progress * 100/line_count, 2)}%) : {try_url}")
            progress += 1


    print(f"Every URL has been processed.")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' does not exist.")
except IOError:
    print(f"Error: Unable to read the file '{file_path}'.")
