from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time





class TinderBot:

    def __init__(self):
        self.driver = webdriver.Chrome()



    #clicks the like button
    def clickLike(self):
        self.likeButton.click()
        print("Clicked")
        time.sleep(3)


    def open(self):
        driver = self.driver
        driver.get('https://tinder.com/app/recs')
        time.sleep(5)
        enter = raw_input('Press enter once logged in\n')
        self.likeButton = self.driver.find_element_by_xpath("//button[@class='button Lts($ls-s) Z(0) Cur(p) Tt(u) Bdrs(50%) P(0) Fw($semibold) recsGamepad__button D(b) Bgc(#fff) Wc($transform) recsGamepad__button--like Scale(1.1):h']")
        #
        #likeButton = driver.find_element_by_xpath("//button[@class='button Lts($ls-s) Z(0) Cur(p) Tt(u) Bdrs(50%) P(0) Fw($semibold) recsGamepad__button D(b) Bgc(#fff) Wc($transform) recsGamepad__button--like Scale(1.1):h']")






Bot = TinderBot()
Bot.open()
Bot.clickLike()
Bot.clickLike()
Bot.clickLike()
Bot.clickLike()
Bot.clickLike()
Bot.clickLike()
