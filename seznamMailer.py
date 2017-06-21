#! /usr/bin/env python3
# seznamMailer.py - Using email.cz, logs in and sends a message given as
# the command lline argument

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

recipient = sys.argv[1]
message = ' '.join(sys.argv[2:])
acc = input("Enter seznam ID: ")
psw = input("Enter seznam password: ")

def mailer(recipient, message):
    browser = webdriver.Chrome('/usr/local/bin/chromedriver')
    browser.get('https://email.cz')
    delay = 5

    try:
        emailElem = WebDriverWait(browser, delay).until(EC.visibility_of_element_located((By.ID, "login-username")))
    except:
        print('Was not able to find the login-username field.')
    emailElem.send_keys(acc)
    emailElem.submit()

    try:
        passwordElem = WebDriverWait(browser, delay).until(EC.visibility_of_element_located((By.ID, "login-password")))
    except:
        print('Was not able to find the login-passwd field.')
    passwordElem.send_keys(psw)
    passwordElem.send_keys(Keys.ENTER)

    try:
        WebDriverWait(browser, delay).until(EC.element_to_be_clickable((By.LINK_TEXT, "Napsat e-mail"))).click()
    except:
        print('Was not able to find the compose button.')

    try:
        toElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/section/div[2]/dl/div[2]/dd/div/input")))
    except:
        print('Was not able to find the "To" field')
    toElem.send_keys(recipient)

    try:
        msgElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "area")))
    except:
        print('Was not able to find the text field')
    msgElem.send_keys(message)

    try:
        WebDriverWait(browser, delay).until(EC.element_to_be_clickable((By.XPATH, "/html/body/section/div[3]/button[1]"))).click()
    except:
        print('Was not able to find the send button')

    try:
        WebDriverWait(browser, delay).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/button[1]"))).click()
    except:
        print('Was not able to find the 2nd send button')
        
mailer(recipient, message)
