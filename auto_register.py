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
keyzard_id = "XXXXX"    # <--- Your Naver blog ID
keyzard_pw = "XXXXX"    # <--- Your Naver blog password (same as your main Naver account)

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
failed_url = []
try:
    with open(file_path, 'r') as file:
        progress = 1

        for line in file:

            sleep(random.uniform(1, 5))

            try_url = line.strip()
            browser.find_element("id", "blogUrl").send_keys(try_url)
            browser.find_element("id", "submit").click()

            wait = WebDriverWait(browser, 60)
            alert = wait.until(expected_conditions.alert_is_present())
            
            if alert.text == "등록되었습니다." or alert.text == "URL이 잘못되었습니다.":
                alert.accept()
                print(f"Processed [{progress}/{line_count}]({round(progress * 100/line_count, 2)}%) : {try_url}")
                progress += 1

                # sometimes, we need to click alert() more to proceed due to site problems.
                try:
                    retry = 0
                    while True:
                        if retry > 0:
                            print(f"Stucked. Try to resolve any remaining alerts... {retry}")
                        alert = browser.switch_to.alert
                        alert.accept()
                        retry += 1
                        sleep(1)
                except:
                    continue
            else:
                print(f"error from alert... [{alert.text}]")
                break


    print(f"Every URL has been processed. There are some URLs failed... {failed_url}")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' does not exist.")
except IOError:
    print(f"Error: Unable to read the file '{file_path}'.")
