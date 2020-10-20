import json as js
import random
import time

import requests
from selenium import webdriver

base_url = "http://xx/"
username = 'xx'
password = 'xx'
min_random_sec = 1
max_random_sec = 3
total_request_count = 5
api_list = []


def login_and_obtain_cookies():
    driver = webdriver.Chrome()

    # 访问网页
    driver.get(base_url)
    time.sleep(max_random_sec)

    # 登录，示例
    driver.find_element_by_class_name('ant-btn').click()
    driver.find_element_by_class_name('tab-login').find_element_by_class_name('right').find_element_by_tag_name(
        'a').click()
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_class_name('btn-login').click()

    # 获取cookies
    c = driver.get_cookies()
    return {c[0]["name"]: c[0]["value"]}


def send_request(c):
    url = base_url + api_list[random.randint(0, len(api_list) - 1)]
    print("send request, url: " + url)
    start = time.time()
    response = requests.get(url, cookies=c)
    print('cost time: {}'.format(time.time() - start))
    print(js.loads(response.text))
    print("-------------------------------")


def main():
    cookies = login_and_obtain_cookies()
    for i in range(total_request_count):
        send_request(cookies)
        time.sleep(random.randint(min_random_sec, max_random_sec))


if __name__ == '__main__':
    main()
