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
{"JBXX":{"XH":"20203202237","XM":"徐喆锴","DWDM_DISPLAY":"电子与信息工程学院","DWDM":"10312","XBDM_DISPLAY":"男","XBDM":"1","LXDH":"18868311022","GJDQ_DISPLAY":"中国","GJDQ":"156","SZDQ_DISPLAY":"安宁区","SZDQ":"620105","RYLB_DISPLAY":"无以上情况","RYLB":"9EBD2B72E1813B21E0530206050ADC67","JJLXR":"钱海峰","JJLXRDH":"15967309777","JJLXRJG_DISPLAY":"浙江省&#x2f;嘉兴市&#x2f;海宁市","JJLXRJG":"330481","JQQK_DISPLAY":"正常","JQQK":"zc","GCKSRQ":"","GCJSRQ":"","SFDFHB_DISPLAY":"否","SFDFHB":"0","DFHTJHBSJ":"","ZDRQJCQK":"","XXDZ":"甘肃省兰州市安宁区安宁西路149","JTXXDZ":"浙江省海宁市海洲桥小区81号","JTXC":"","JQQTQK":"","XSBH":"20203202237"},"MRQK":{"WID":"e81aae357a7b4e1f88f266f6b7af266f","XSBH":"20203202237","TBSJ":"2021-10-30","TW":"36.4","BRJKZT_DISPLAY":"正常","BRJKZT":"1","SFJZ_DISPLAY":"否","SFJZ":"0","JTCYJKZK_DISPLAY":"正常","JTCYJKZK":"1","XLZK_DISPLAY":"无","XLZK":"www","MRSZDQ_DISPLAY":"甘肃省&#x2f;兰州市&#x2f;安宁区","MRSZDQ":"620105","MRXXDZ":"桃海学生公寓","QTQK":""}}