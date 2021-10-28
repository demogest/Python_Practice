from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Chrome()
browser.get("https://ehall.lzjtu.edu.cn/")
browser.find_element(By.CSS_SELECTOR,"div[class='amp-has-nologin-btn  amp-animated amp-animate-move-bottom-in amp-hover-slow-motion']").click()
browser.find_element(By.XPATH,'//input[@name="username"]').send_keys('20203202237')
browser.find_element(By.XPATH,'//input[@id="password"]').send_keys('?!Hnzk2002')
browser.find_element(By.XPATH,'//button[@class="auth_login_btn primary full_width"]').click()
time.sleep(5)
browser.find_element(By.XPATH,'//div[@data-i18n="availableApps"]').click()
time.sleep(3)
browser.find_element(By.XPATH,'//div[@amp-title="学生报平安"]').click()
time.sleep(1)
browser.find_element(By.XPATH,'//div[@class="amp-detail-enter amp-active"]').click()
time.sleep(10)