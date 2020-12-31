from infoForAct import username,password,person,message
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# Version 0.1
# New updates will be added in 2021

class Instagram:
    def __init__(self,username,password,aranan,mesaj):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.person = person
        self.message = message

    def signIn(self):
        self.browser.get("https://www.instagram.com/direct/new/")
        time.sleep(3) # For load the page
        
        usernameInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(45) # For Two Factor Authentication.      You can reduce the time if you don't use 2FA
    def sendMessage(self):
        sendInfo1 = self.browser.find_element_by_name('queryBox')
        sendInfo1.send_keys(self.person)
        
        time.sleep(4)
        sendInfo = self.browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/button/span").click()
        time.sleep(5)
        self.browser.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[2]/div/button/div").click()
        time.sleep(4)
        messageBox = self.browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
        messageBox.send_keys(self.message)
        time.sleep(3)
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
        


instgrm = Instagram(username,password,person,message)
instgrm.signIn()
instgrm.sendMessage()