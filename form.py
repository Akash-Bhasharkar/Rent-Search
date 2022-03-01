from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
from data import Data

FORM_LINK = "" #Google form link

chrome_driver_path = "C:/Akki/chromedriver"




class Form(Data) :

    def __init__(self) :
        super().__init__()
        
        self.driver = webdriver.Chrome(executable_path = chrome_driver_path)

    
    def fill_form(self) :
        addr_list = self.rent_address()
        link_list = self.rent_link()
        price_list = self.rent_price()

        for index in range(len(addr_list)) :
            self.driver.get(FORM_LINK)

            time.sleep(2)
            self.addr = self.driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
            self.link = self.driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
            self.price = self.driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
            
            time.sleep(2)

            self.addr.send_keys(addr_list[index])
            time.sleep(1)

            self.price.send_keys(price_list[index])
            time.sleep(1)

            self.link.send_keys(link_list[index])
            time.sleep(1)

            self.submit = self.driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div/div")
            self.submit.click()

            time.sleep(5)