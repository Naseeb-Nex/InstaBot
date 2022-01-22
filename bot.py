from selenium import webdriver
import os
import time



class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'
        self.driver = webdriver.Chrome('./chromedriver.exe')

        self.login()
    


    def login(self):
        self.driver.get('{}/accounts/login/'.format(self.base_url))
        time.sleep(5)

        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(self.username)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(self.password)
        self.driver.find_elements_by_xpath("//div[contains(text(), 'Log In')]")[0].click()
        time.sleep(5)

    def nav_user(self, user):
        self.driver.get('{}/{}/'.format(self.base_url, user))

    def follow_user(self, user):

         self.nav_user(user)

         follow_button = self.driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")[0]
         follow_button.click()

     
if __name__ == '__main__':


    instabot = InstagramBot('_crazy_pilot_', 'naseeb123')
    # instabot.nav_user('favas_abdulsamad')
    instabot.follow_user('favas_abdulsamad')