# encoding = "utf-8"
# !/usr/bin/env python3

import threading
import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


def main():
    driver: WebDriver = webdriver.Chrome(executable_path="./chromedriver")
    driver.get("https://www.taobao.com/")
    driver.find_element_by_link_text("亲，请登录").click()
    # 等待用户登录

    while True:
        if not "login.taobao.com" in driver.current_url: break
        time.sleep(20)

        # 开始进入页面
        driver.get("https://detail.tmall.com/item.htm?id=624108229863&ali_refid=a3_430583_1006:1104469610:N:elW8lzZemj5wF2Tr8AKxfA==:48009ec0287277458610d985947840cb&ali_trackid=1_48009ec0287277458610d985947840cb&spm=a230r.1.14.1&skuId=4680050034680")
        # 调起多线程
        threads = buy_thread(driver)
        threads.start()
        threads.join()
        driver.quit()


class buy_thread(threading.Thread):
    def __init__(self, driver):
        threading.Thread.__init__(self)
        self.daemon = True
        self.driver = driver

    def run(self):
        while True:
            if '01:12:00' in str(time.asctime()):
                print("time.asctime()"+time.asctime())
                while True:
                    try:
                        self.driver.find_element_by_link_text("立即购买").click()
                        break
                    except Exception as e:
                        print(e)

                while True:
                    try:
                        self.driver.find_element_by_link_text('提交订单').click()
                        input()
                    except Exception as e:
                        print(e)
            time.sleep(0.01)


if __name__ == '__main__':
    main()
