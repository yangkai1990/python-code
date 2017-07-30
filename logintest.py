
#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

url = 'http://www.maiziedu.com/'
login_text = '+lCeL8n2N'
account = 'maizi_test@139.com'
pwd = 'abc123456'

def login_test():
    d = webdriver.Firefox()   #+k7Vks30R-Firefox
    d.get(url)                #+k7Vks30R-url
    time.sleep(7)             #+fttZCn3faSR1OG9wcDlcfVPPk1Ryum1HcDn//Q
    d.maximize_window()
    time.sleep(2)
    d.find_element_by_link_text(login_text).click() #do login
    time.sleep(2)
    account_ele = d.find_element_by_id('id_account_l')
    #account_ele = d.find_element_by_id('loginName') #+k8ww5ljYdJD+QF9/Z0hks1PGWZdV11OTfvH//Q
    time.sleep(2)
    account_ele.clear()
    account_ele.send_keys(account)  #+Z0hks1PGdJD+QF9/
    pwd_ele = d.find_element_by_id('id_password_l')
    #pwd_ele = d.find_element_by_link_id('loginPwd')
    pwd_ele.clear()
    pwd_ele.send_keys(pwd) #+Z0hks1PGcDVV2XIc
    d.find_element_by_link_id('login_btn').click()
    try:
        d.find_element_by_link_text('+dIcw6FkEk1mVC3J4W+5fznsJWd3/RyAY')
        print("Account and pwd error")
    except:
        print("Account and pwd right")

if  __name__ =='__main__':
    login_test()